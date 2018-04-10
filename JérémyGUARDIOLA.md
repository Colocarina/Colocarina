# 9 Avril 2018

Après avoir reçu la carte Raspberry Pi 3, nous avons essayé de la faire marcher avec l'écran que M. Masson nous a fourni. Malheureusement, malgré avoir suivi plusieurs différents tutoriels les uns après les autres, cela ne nous donnait toujours rien. Nous avons donc contacté d'autres PeiP2 utilisant une carte RaspBerry qui ont reussi à nous mettre sur la voie de la réussite car le soir même, la carte fonctionnait. Il ne reste plus qu'à tester le programme que nous possédons déjà. De plus, nous avons fait l'inventaire en détail de tout le matériel nécessaire à la fabrication de chaque module.

# 5 Avril 2018

Ce jour-ci fut le jour de présentation de mi-parcours. A vrai dire, vu notre retard du à une accumulation de problème de programation, nous n'avions pas grand chose à dire. Durant cette séance, on a essayé de continuer un programme qui stockerait toutes les données dans des tableaux, en vain. On a finalement decidé de s'arrêter pour réfléchir et se demander si ce que l'on fesait était nécessaire. Nous nous sommes rendus compte que nous perdions un maximum de temps sur un objet sensé être temporaire dans notre projet. On en a discuté avec M. Ferrero pour finaler décider de repartir sur notre projet initial, la reconnaissance sonore.

# 29 Mars 2018

Après avoir réussi la séance précédente à programmer la reconnaissance des notes, il nous fallait réussir à les stocker dans un endroit durant une certaine durée (donc inclure la notion de temps dans le programme), à en extraire uniquement les notes utiles puis à comparer ces données à d'autres où serait stocké les musiques. Mais la notion de tableau dynamique est apparu beaucoup plus complexe (surtout impossible sachant notre niveau informatique), ce qui nous a pris tout le temps de la séance après avoir régler le problème de temps.

# 16 Mars 2018

Avec Marylou, nous avons essayé de comprendre un peu plus le language d'Arduino (en gros C++) pour pouvoir coder notre programme principal qui va analyser les informations transmises par les boutons poussoires (c'est à dire les notes jouées) et ainsi selon les notes jouées à la suite, correspondre à une musique, et de ce fait, appliquer une tâche. 
Nous avons donc commencé, mais nous nous sommes heurtés à plusieurs complications ce qui a ralenti l'avancée du programme. Au final, nous avons réussi à programmer la reconnaissance des notes et le fait de retourner une valeur qui pourra être analysé dans notre prochaine fonction, celle qui comprendra la musique jouée et qui renverra une fonction.

# 07 Février 2018

Durant cette heure et demi, nous avons fini notre "ocarina informatique" après avoir contré plusieurs soucis techniques et découvert la librairie Tone. Nous pourrons donc nous pencher sérieusement dès à présent sur les fonctions et la wifi.

# 23 Janvier 2018

Aujourd'hui a eu lieu la présentation orale de notre projet. Nous avons donc présenté notre borne domotique à toute la classe et à la fin, M. Masson nous a conseillé qu'il fallait mieux se focaliser sur les différentes fonctions et la manière dont on enverra l'information aux différents modules, avant de chercher à maitriser la reconnaissance sonore. Nous avons donc matérialisé "un ocarina informatique", c'est à dire que la musique serait produite par un buzzer arduino dont les notes seraient gérés informatiquement et non pas par reconnaissance. Et en parallèle à cela, nous avons écouté les différents projets de nos camarades. 

# 18 Janvier 2018

Après le choix des matériaux nécessaires, M. Masson nous a soulevé une interrogation, comment brancher notre micro sur l'Arduino ? En effet, la manière dont on l'avait imaginé n'était pas réaliste car il n'y aurait pas eu d'alimentation. Nous avons donc décidé de partir sur une carte Raspberry pi 3, équipé de ports usb où l'on peut brancher le micro, jack pour l'enceinte, micro usb pour l'alimentation ainsi qu'une carte wifi intégré. Ainsi, tous nos besoins seront centralisé en cette carte.
Ensuite, nous avons commencé à conceptualiser le projet en nous intéressant aux différents branchements et spécifiant les matériaux nécessaires pour chaque fonction. 
Enfin, nous avons continué la présentation du projet.

# 12 Janvier 2018

Lors de cette 2ème séance, nous avons fait une sorte de brainstorming en développant nos idées en nous concentrant sur ce que l'on doit commander, et comment cela fonctionnera. 
De plus, nous avons regardé une vidéo en anglais (https://www.youtube.com/watch?v=1RzXoieos5Y), nous décrivant comment le projet pourra fonctionner. Dans la description de cette vidéo, les programmes et quelques composants nous sont donnés pour nous aider dans la conception du projet.
Enfin, nous avons démarré la présentation du projet qui aura lieu à la fin du semestre.

# 22 Décembre 2017

Aujourd'hui nous avons élaboré notre projet autour d'une passion commune, la musique. 
Cela correspond à une borne domotique sans fil commandé par la musique d’un Ocarina. 
Nous avons choisi différentes tâches que notre Ocarina pourra dirigé en fonction des notes jouées.
Il pourra :	Allumer une lampe (intensité lumineuse ?), Déverrouiller une porte, Annoncer l’heure par un réveil, Appeler pour retrouver son téléphone
De plus, nous avons créé notre page Github.
