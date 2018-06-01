/*
Programme emprunté du projet Zelda Home Automation disponible sur GitHub
Programme téléversé sur la carte ESP32 du module Lampe
*/
#include <WiFi.h> //ESP32
#include <PubSubClient.h> 
#include <Servo.h>

Servo myservo;

// Update these with values suitable for your network.
const char* ssid = "Mr banana";
const char* password = "bananequiflambe";
const char* mqtt_server = "192.168.43.86";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;
int n=0;

////////////////////////////////////////////CHOOSE WHICH SONG RECEIVER HERE!!!
//'1' = Sun;
//'2' = Time;
//'3' = Saria;
//'4' = Zelda;
//'5' = Heal;
char song = '1';
/*Sun's Song, Song of Storms, and Minuet of Forest are
 * all executed by a single esp8266 controlling multiple relays
 */
int outPin = 2;
//int stormPin = 4;
//int forestPin = 5;
//int pause = 0;
//int stormPause;
//int forestPause;
int angle;
int neutral;
int bounce;
boolean toggle = true;

void setup() {
  //pinMode(BUILTIN_LED, OUTPUT);// Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  myservo.attach(outPin);

  if (song=='1') {
    myservo.write(9);
  }
  
  if (song=='4') {//zelda
    myservo.write(90);
  }
}

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Do the thing if your song plays
  /*if ((char)payload[0]=='3'&&song=='1') {
    pinToggle(stormPin);//storms
  }
  if ((char)payload[0]=='4'&&song=='1') {
    pinHold(forestPause, forestPin);//forest
  }*/
  if ((char)payload[0] == song) {
    if (song=='1') {//Sun
      servoHold();
    }
    if (song=='4') {//Zelda
      servoToggle();
    }
/*    if (song=='2') {//time
       pinHold(pause, outPin);
    }
    if (song=='5'){//heal
      servoHeal();
    }
    if (song=='1') {
      pinToggle(outPin);//sun
    }*/
  }
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("Sun")) {///////////////THIS MUST BE A UNIQUE NAME FOR EACH ESP8266
      //Time
      //Epona
      //SunStormForest
      //Fire
      //Zelda
      Serial.println("connected");
      // Once connected, publish an announcement...
      //client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("songID");
    }
    else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    ++value;
    snprintf (msg, 75, "hello world #%ld", song);
    Serial.print("Publish message: ");
    Serial.println(msg);
    //client.publish("outTopic", msg);
  }
}

/*void pinToggle(int pin) {//toggle pin high/low whenever song is heard
  digitalWrite(pin, !digitalRead(pin));
}*/
//void pinHold(int holdTime, int pin) {//hold pin low for some time when song is heard, then go back high
//  digitalWrite(pin, LOW);
//  delay(holdTime);
//  digitalWrite(pin, HIGH);
//}

void servoToggle() {//bring servo to position, bounce back a bit, hold until song plays again then move back+bounce
  if (toggle) {
    myservo.write(9);
  } 
  else {
      myservo.write(90);
  }
  toggle = !toggle; 
}

void servoHold() {//when song is heard move servo to some position then move it back to neutral
  myservo.write(90);
  delay(1000);
  myservo.write(9);
  //n+=1%4;
}

//void servoHeal(){
//  toggle=!toggle;
//  servoHold();
//
//  while (n!=0){
//    servoHold();
//  }
//}



