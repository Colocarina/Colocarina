# 1er Juin 2018
# Fin du projet

Aujourd'hui nous avon procédé aux derniers réglages de notre projet, à la finalisation du rapport et de notre présentation orale. Ce projet a été très enrichissant et nous a appris à travailler en groupe et en autonomie. De plus il est intéressant de pouvoir travailler sur un sujet que l'on a choisit par soi même.

# 30 Mai 2018

Notre projet est fonctionnel (pour les deux modules fabriqués: lampe et verrou) lorsqu'il est branché à un ordinateur. Mais les cartes wifi ne sont pas autonomes et se déconnectent du mqtt lorsqu'elles sont seules. Nous avons trouvé la solution à ce problème, il faut brancher les servo moteurs sur le 3V3 de l'esp et non sur le 5V.
A présent notre projet fonctionne, les esp se connectent correctemement au Wifi et lorsque l'on joue une mélodie les servo moteurs agissent.

# 24 Mai 2018

Nous avons été au FabLab aujourd'hui et finit de créer nos deux modules (lampe et verrou). Il ne reste plus qu'à réussir à faire fonctionner les esp32 pour qu'elles fassent bouger les servo moteurs fixés dans les modules. (voir photos dans le rapport)
Nous avons aussi réussis à faire fonctionner le programme pyhton sur la raspberry. Lorsque l'on branche le micro et que l'on produit un son, si la note est reconnue elle est affichée et sinon la phrase "Pardon? Je n'ai pas bien saisis" est affichée. Lorsque l'on joue la mélodie d'une fonction, le nom de la mélodie est affichée. Il ne reste donc plus qu'à réussir à faire fonctionner les cartes Wifi.

# 19 Mai 2018

Nous nous sommes résolu à arrêter de s'obstiner à utiliser la raspberry pour téléverser sur les esp. Après avoir essayé de téléverser le programme .ino sur les esp depuis un ordinateur, tout fonctionne à merveille. Le concept du projet est donc d'utiliser le fichier .ino sur les esp32 et le fichier .py sur la raspberry. Un ami m'a aidé à comprendre le concept d'une carte wifi, il faut connecter les composants à relier entre eux au même réseau wifi pour qu'ils puissent communiquer. Nous avons aussi réussis à faire fonctionner le mqtt grâce à la commande sudo /etc/init.d/mosquitto stop   . En effet le broker mqtt se lance au démarrage de l'ordinateur et lorsque l'on veut le relancer depuis le terminal, cela provoque une erreur.

# 13 Mai 2018

Le protocole MQTT ne fonctionne pas, nous avons une erreur d'IPv6 (sans savoir vraiment d'où cela vient). De plus Ubuntu a planté (car nous avons beaucoup utilisé la Raspberry pendant ce weekend qui a sûrement surchauffé) donc nous avons dû tout réinstaller. De plus les librairies ESP32 ne fonctionnent toujours pas, nous ne savons pas vraiment comment nous allons réussir à lancer les programmes. Nous ne savons pas vraiment comment utiliser le  Wifi (quel wifi utiliser, la raspberry doit elle servir de Hotspot, ou est-ce les esp qui créent le Wifi). Il va nous falloir approfondire tout cela et demander conseil.

# 29 Avril 2018

Nous continuons a visionner la vidéo d'explication disponible sur youtube du projet Zelda Home Automation et recherchons à présent à faire fonctionner le protocole MQTT (mosquitto) sur la Raspberry. Nous épluchons les sites internet pour comprendre ce principe de fonctionnement mais des erreurs nous sont affichées sur le terminal donc cela ne paraît pas encore vriament fonctionnel. De plus Firefox ne fonctionne plus sur la Raspberry et après avoir essayé toutes les solutions qu'on a trouvé sur internet la dernière solution qui s'offre à nous est de réinstaller Ubuntu. Firefox nous étant utile pour rechercher des packages, plus pratique qu'un terminal.

# 15 Avril 2018
L'avancée du projet est ralentie par notre emploi du temps chargé, notre problème actuel est de faire fonctionner arduino IDE sur la raspberry mais nous avons des problèmes de bibliothèque . En effet nous avons installé la bibliothèque expressif/esp32 (disponible sur GitHub https://github.com/espressif/arduino-esp32) mais lorsque nous téléversons sur l'esp32 une erreur de fichier manquant apparaît et nous ne savons pas comment remédier à ce problème. Nous cherchons des solutions sur internet en épluchant tous les sites en espérant trouver une solution efficace.

# 09 Avril 2018
# 9ème séance

Nous avons reçu notre carte Raspberry et commencé à essayer de nous en servir. Cela paraît encore compliqué, même en suivant les tutoriels impopssible d'avoir un affichage sur l'écran LCD. nous avons donc demandé de l'aide à des amis de PeiP2 se servant aussi de Raspberry dans leurs projets. Avec leur aide nous avons réussis à avoir ubuntu sur notre raspberry et d'afficher le bureau sur l'écran d'une télévision, mais par sur l'écran LCD. Vu les lignes blanches affichées par l'écran nous en déduisons que l'écran doit être défecteux. Nous avons donc commandé un nouvel écran à M Masson. En attendant la réception de cet écran nous travaillons sur l'écran de télévison.

# 05 Avril 2018
# 8ème séance

Nous avons passé aujourd'hui notre oral de mi-parcourt, sans être vraiment à mi-parcourt. En effet nous n'arrivons pas à créer de programme et nous doutons de l'utilité de ce que  nous avons fait jusque là. En effet notre projet se basant en grande partie sur le projet Zelda Home Automation (disponible sur GitHub). Nous avons donc décider d'arrêter d'essayer en vain, et de suivre le projet duquel on s'inspire à la base. Donc avec les conseils de M Ferrero nous avons décidé d'utiliser une Raspberry, plus apte à la reconnaissance sonore.

# 29 Mars 2018
# 7ème séance

Nous avons continué notre programme en introduisant les notions de tableau dynamique pour pouvoir stocker des séquences de notes jouées afin de pouvoir les comparer à une mélodie de base. Mais cette notion s'avère très complexe et nous ne parevenons pas à toucher à notre but. 

# 16 Mars 2018
# 6ème séance

Nous avons poursuivis notre programme pour que en fonction des boutons poussoirs enfoncés, lorsqu'on joue une mélodie précise une musique soit retournée. Pour se faire nous travaillons donc à mieux comprendre le fonctionnement de C++ et ses fonctions car nous avons beaucoup de problèmes de compilations. Mais nous sommes encore toujours loin de réussir à interpréter les notes d'un ocarina. 

# 07 Février
# 5ème séance

Nous avons continué le programme, nous l'avons enrichi avec la librairie Tone. Nous cherchons des solutions au traitement de la suite de "notes" c'est à dire la redirection vers les différentes tâches.

# 23 Janvier 2018
# 4ème séance

Durant cette séance nous avons présenté notre projet à l'oral. M Masson nous a conseillé de ne pas trop s'attarder pour l'instant sur la reconnaissance sonore pour plutôt se focaliser sur la programmation. Nous avons donc mis en oeuvre un ocarina électronique. Grâce auquel la reconnaissance sonore n'est pas mis en oeuvre, les notes sont reconnues en fonction des boutons poussoirs enfoncés. Le son produit par le buzzer est juste pour nous représenter ce qu'il se passe.


# 18 Janvier 2018
# 3ème séance

Durant la semaine nous avons réfléchis au marèriel necessaire et envoyé une premère commande.
Nous nous sommes rendu compte que la carte arduino présenterait des probèmes de compatibilité avec le micro (port USB), de ce fait nous nous sommes orienté vers l'utisation d'une carte Rasperry PI 3 Wifi, plus adaptée grâce à ses ports USB et jack et la présence intrinsèque de Wifi.
Donc finalement nous brancherons notre micro USB à la carte Raspberry, et cette dernière sera alimentée par secteur. Le port jack nous servira à brancher une petite enceinte qui enverra un son de confirmation lorsque la tâche sera bien prise en compte. 



# 12 Janvier 2018
# 2ème séance

Pendant cette séance nous avons regardé une vidéo (https://www.youtube.com/watch?v=1RzXoieos5Y) décrivant le fonctionnement de la borne. Dans la description de la vidéo on a trouvé les codes pour la carte raspberry sous le logiciel Arduino et python ayant servit au projet, nous devrons donc déchiffrer et adapter ce code. On a aussi répertorié le materiel dont nous allons avoir besoin tel que la carte wifi ESP32.
On a ensuite commencé le powerpoint à présenter à la fin du semestre. Commençant à dégrossir un planning et une répartition des tâches.



# 22 Décembre 2017 
# 1ère séance

Aujourd'hui nous avons fixé les conditions de notre projet. Nous avons établi les tâches qui seraient possiblement
faisables à notre échelle.
Nous avons créé notre page Github et commencé la description du projet sur la page.
Il y a encore de nombreuses recherches à effectuer quand à savoir le matèriel necessaire et la manière dont nous allons 
concevoir le système. Nous avons un peu commencé ces recherches, le site suivant pourra beaucoup nous aider 
https://www.raspberrypi.org/blog/zelda-home-automation/
