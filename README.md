![Polytech](https://camo.githubusercontent.com/2fe98f1f93a495607acfac1a6b62cb1d4affdbca/687474703a2f2f7777772e706f6c79746563686e6963652e66722f6a616869612f6a73702f6a616869612f74656d706c617465732f696e632f696d672f706f6c79746563685f6e6963652d736f706869612e706e67)

Ce projet est réalisé dans le cadre de la formation de prépa intégrée de Polytech'Nice Sophia


# Colocarina

# Description du Projet :

Borne domotique sans fil commandé par la musique d’un Ocarina. Différenciations des tâches en fonction des notes jouées. 

Les taches possibles de notre borne domotique sont allumer une lampe et déverrouiller une porte

# Materiel utilisé : 

- Raspberry PI 3 + écran LCD + clavier + souris
- ESP 32
- Ocarina
- Microphone branchable en USB
- Servo-moteur
- Lampe, verrou et piles


# Principe de fonctionnement : 

La borne est constituée d'une carte Raspberry PI 3 servant de broker MQTT (mode de communication fonctionnant sur un principe de publish/subscribe). Cette dernière analyse le son joué par l'ocarina à l'aide d'un microphone branché en USB et du programme python AnalyseAudio.py. 

Les modules sont constitués principalement d'une carte Wifi ESP32 et de servomoteurs. La carte Wifi reçoit les informations de la Raspberry et agit en conséquence. Les programmes téléversés dans les ESP32 sont respectivement Sun.ino pour la carte du module Lampe et Zelda.ino pour la carte du module Verrou.

Raspberry et ESP32 communiquent par publications et souscriptions. La Raspberry publie sur l'ESP32 le numéro de la mélodie qu'elle a identifié et l'ESP32 souscrit à cette publication. Le programme .ino effectue alors la fonction correspondant à ce numéro.

# Sources du projet : 

Projet réalisé par Allen Pan

  Lien vers les sources de nos programmes :
  
https://github.com/Sufficiently-Advanced/ZeldaHomeAutomation

  Lien vers des vidéos explicatives :
  
https://www.youtube.com/watch?v=glZnkpIDWSE

https://www.youtube.com/watch?v=1RzXoieos5Y
