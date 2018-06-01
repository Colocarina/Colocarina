#Tone detection shamelessly stolen from:
#https://benchodroff.com/2017/02/18/using-a-raspberry-pi-with-a-microphone-to-hear-an-audio-alarm-using-fft-in-python/
#!/usr/bin/env python
import pyaudio
from numpy import zeros,linspace,short,fromstring,hstack,transpose,log
from scipy import fft
from time import sleep
from collections import deque
import paho.mqtt.client as mqtt
import requests
import pygame.mixer
from pygame.mixer import Sound
#import RPi.GPIO as GPIO

###GPIO stuff
##GPIO.setmode(GPIO.BCM)
##GPIO.setup(5, GPIO.OUT)#D4 Blue
##GPIO.setup(6, GPIO.OUT)#F Down
##GPIO.setup(13, GPIO.OUT)#A Right
##GPIO.setup(19, GPIO.OUT)#D5 Up
##GPIO.setup(26, GPIO.OUT)#B Left
##
##GPIO.output(5, GPIO.LOW)
##GPIO.output(6, GPIO.LOW)
##GPIO.output(13, GPIO.LOW)
##GPIO.output(19, GPIO.LOW)
##GPIO.output(26, GPIO.LOW)
#audio stuff maybe
pygame.mixer.init(32000)
confirm = Sound("Music/OOT_Song_Correct.wav")#change accordingly for your song confirmation sound file name/location
#mqtt stuff
client = mqtt.Client()
client.connect("localhost",1883,300)

#Volume Sensitivity, 0.05: Extremely Sensitive, may give false alarms
#             0.1: Probably Ideal volume
#             1: Poorly sensitive, will only go off for relatively loud
SENSITIVITY= 1.0

#Bandwidth for detection (i.e., detect frequencies within this margin of error of the TONE)
BANDWIDTH = 25

# Alarm frequencies (Hz) to detect (Use audacity to record a wave and then do Analyze->Plot Spectrum)
A=460
B=525
C=560
D=622
E=680
#F=735
#G=815
#A5=890
#frequency ranges for each note
'''rangeD4 = range(D4-BANDWIDTH,D4+BANDWIDTH)
rangeE = range(E-BANDWIDTH,E+BANDWIDTH)
rangeF = range(F-BANDWIDTH,F+BANDWIDTH)
rangeG = range(G-BANDWIDTH,G+BANDWIDTH)
rangeA = range(A-BANDWIDTH,A+BANDWIDTH)
rangeB = range(B-BANDWIDTH,B+BANDWIDTH)
rangeD5 = range(D5-BANDWIDTH,D5+BANDWIDTH)'''
#These numbers work for my ocarina in my house with a blue yeti, ymmv
minA = A-50
maxA = A+BANDWIDTH
minB = B-BANDWIDTH
maxB = B+12
minC = C-12
maxC = C+BANDWIDTH
minD = D-BANDWIDTH
maxD = D+BANDWIDTH
minE = E-BANDWIDTH
maxE = E+BANDWIDTH
##minF = F-BANDWIDTH
##maxF = F+BANDWIDTH
##minG = G-BANDWIDTH
##maxG = G+BANDWIDTH
##minA4 = A-BANDWIDTH
##maxA4 = A+55


# Song note sequences
Sun = deque(['E','D','C','A','B','C'])
Time = deque(['A','E','A','D','A','C'])
Saria = deque(['D','C','B','A','B','A'])
Zelda = deque(['C','A','D','C','A','D'])

Heal = deque(['B','A3','E','B','A','E'])
Test = deque(['C','A3','C','A3','C','A3']) #Not a Zelda song, just nice to make sure everything's working
#heard note sequence deque
notes = deque(['C','C','C','C','C','C'], maxlen=6)

# Show the most intense frequency detected (useful for configuration)
frequencyoutput=True
freqNow = 1.0
freqPast = 1.0

#Set up audio sampler - 
NUM_SAMPLES = 2048
SAMPLING_RATE = 44100 #make sure this matches the sampling rate of your mic!
pa = pyaudio.PyAudio()
_stream = pa.open(format=pyaudio.paInt16,
                  channels=1, rate=SAMPLING_RATE,
                  input=True,
                  frames_per_buffer=NUM_SAMPLES)

#print("Alarm detector working. Press CTRL-C to quit.")

while True:
    while _stream.get_read_available()< NUM_SAMPLES: sleep(0.01)
    audio_data  = fromstring(_stream.read(
        _stream.get_read_available()), dtype=short)[-NUM_SAMPLES:]
    # Each data point is a signed 16 bit number, so we can normalize by dividing 32*1024
    normalized_data = audio_data / 32768.0
    intensity = abs(fft(normalized_data))[:NUM_SAMPLES/2]
    frequencies = linspace(0.0, float(SAMPLING_RATE)/2, num=NUM_SAMPLES/2)
    if frequencyoutput:
        which = intensity[1:].argmax()+1
        # use quadratic interpolation around the max
        if which != len(intensity)-1:
            y0,y1,y2 = log(intensity[which-1:which+2:])
            x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
            # find the frequency and output it
            freqPast = freqNow
            freqNow = (which+x1)*SAMPLING_RATE/NUM_SAMPLES
        else:
            freqNow = which*SAMPLING_RATE/NUM_SAMPLES
       # print "\t\t\t\tfreq=",freqNow,"\t",freqPast
    if minA <= freqPast <= maxE and abs(freqNow-freqPast) <= 25:
        if minA<=freqPast<=maxA and minA<=freqNow<=maxA and notes[-1]!='A':
            notes.append('A')
##	    GPIO.output(26, GPIO.LOW)
##	    GPIO.output(19, GPIO.LOW)
##	    GPIO.output(13, GPIO.HIGH)
##	    GPIO.output(6, GPIO.LOW)
##	    GPIO.output(5, GPIO.LOW)
            print "You played A!"
        elif minB<=freqPast<=maxB and minB<=freqNow<=maxB and notes[-1]!='B':
            notes.append('B')
##	    GPIO.output(26, GPIO.LOW)
##	    GPIO.output(19, GPIO.LOW)
##	    GPIO.output(13, GPIO.LOW)
##	    GPIO.output(6, GPIO.HIGH)
##	    GPIO.output(5, GPIO.LOW)
            print "You played B!"
        elif minC<=freqPast<=maxC and minC<=freqNow<=maxC and notes[-1]!='C':
            notes.append('C')
##	    GPIO.output(26, GPIO.HIGH)
##	    GPIO.output(19, GPIO.LOW)
##	    GPIO.output(13, GPIO.LOW)
##	    GPIO.output(6, GPIO.LOW)
##	    GPIO.output(5, GPIO.LOW)
            print "You played C!"
        
        elif minD <= freqPast <= maxD and minD <= freqNow <= maxD and notes[-1]!='D':
            notes.append('D')
##	    GPIO.output(26, GPIO.LOW)
##	    GPIO.output(19, GPIO.HIGH)
##	    GPIO.output(13, GPIO.LOW)
##	    GPIO.output(6, GPIO.LOW)
##	    GPIO.output(5, GPIO.LOW)
            print "You played D!"
        
        elif minE<=freqPast<=maxE and minE<=freqNow<=maxE and notes[-1]!='E':
            notes.append('E')
##	    GPIO.output(26, GPIO.HIGH)
##	    GPIO.output(19, GPIO.LOW)
##	    GPIO.output(13, GPIO.LOW)
##	    GPIO.output(6, GPIO.LOW)
##	    GPIO.output(5, GPIO.LOW)
            print "You played E!"
        else:
            print "What the heck is that?"#prints when sound is in range but not identifiable as note
											#or when a note has already been registered and is "heard" again

    if notes==Sun:
        print "\t\t\t\tSun song!"
	client.publish("songID", "1") #1=Sun
	confirm.play()
	notes.append('C')#append with 'G' to 'reset' notes, this keeps the song from triggering constantly
    if notes==Time:
        print "song of Time!"
	client.publish("songID", "2") #2=Time
	confirm.play()
	notes.append('C')
    if notes==Saria:
        print "Saria's song!" #3=Saria
	_stream.stop_stream()
	requests.post("https://maker.ifttt.com/trigger/YOUR_EVENT_NAME/with/key/YOUR_KEY")#You'll need your own Maker account and ifttt event
	notes.append('C')
	confirm.play()
	_stream.start_stream()
    if notes==Zelda:
        print "\t\t\t\tZelda's Lullaby!"
        client.publish("songID", "4") #4=Zelda
	confirm.play()	
	notes.append('C')
    if notes==Heal:
	print "Song of Healing!"
	_stream.stop_stream()
	confirm.play()
	sleep(20)
	client.publish("songID", "5")
	notes.append('C')
	_stream.start_stream()
    if notes==Test:
        print "Test Sequence Activated!"
        confirm.play()
        notes.append('C')
