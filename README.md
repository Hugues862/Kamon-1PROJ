# Documentation Technique

## Documentation

> Le but de cette documentation technique est de vous expliquer les différents choix techniques que nous avons mis en place durant ce projet.

## Window :

> Au péalable installer Pillow

- Pour installer le framework Pillow mis à jour sur votre machine Windows, exécutez le code suivant dans votre ligne de commande ou dans Powershell :

      -python3 -m pip install --upgrade pip
      -python3 -m pip install --upgrade Pillow
      -pip install Pillow

## Mac :

- Ouvrez Terminal (Applications/Terminal) et exécutez :

        -xcode-select -install
        -sudo easy_install pip
        -sudo pip install pillow
        -pip install pillow

## Présentation des différents modes de jeu :

- Dans cette partie nous allons vous expliquer comment faire pour lancer les différent mode de jeu :

  ### Mode 1 contre 1

      Version du jeu ou deux joueurs s’affrontent sur le même ordinateur
          - Entrer préalablement les pseudos du joueur 1 et du joueur 2
          - Lancer la partie avec bouton en bas de la fenêtre

  ### Mode en ligne

      Une version du jeu ou deux joueurs s’affrontent en réseau sur deux machines différentes.
          - Entrer soit l'IP de l'hôte qui a créer la partie
          - Créer une partie en donnant l'IP au deuxième joueur
          - Lancer la partie avec bouton en bas de la fenêtre

  ### Mode IA

      Une version du jeu ou un joueur humain joue contre une intelligence artificielle, ce dernier choisissant ses coups de manière aléatoire
          - Entrer préalablement les pseudos du joueur 1 et du joueur 2
          - Lancer la partie avec bouton en bas de la fenêtre

## Justification du choix du langage et de la librairie graphique.

### Pourquoi avons nous utilisés le langage Python ?

- Nous avons plus aisance sur le langage Python grâce aux différents modules qu’on a pu avoir au cours de l’année
- Nous avons plus de facilité à utiliser python car nous avons auparavant déjà réaliser des projets avec ce langage.
- Python dispose d’une Bibliothèques étendues qui permet d’utiliser le code à des fins diverses
- Python est un langage assez Facile à apprendre, comprendre, et coder.

### Pourquoi avons nous utilisés la librarie graphique TKINTER ?

> Nous avons utilisé la librairie TKINTER afin de pouvoir créer une interface graphique au jeu que nous avons voulu implémenté

- Auparavant nous avons eu l’occasion de réaliser des projet grâce a cette librairie, ce qui nous a donner un petit avantage.
- La librairie TKINTER est très simple d’utilisation, elle a de nombreuse fonctionnalité qui nous a permis d’améliorer le design et l’ergonomie afin que l’utilisateur puisse jouer dans de bonne condition.

## Description des structures de données.

> Pour ce qui est de la structure on établit en premier lieu un dossier src pour contenir les fichier système de l’entièreté du jeu à l’intérieur de ce src on trouvera les dossiers assets et commun :

- Le dossier assets contiendras l’ensemble des supports visuels (images) afin de dynamiser son usage et de s’organiser selon nos différents supports

- Le dossier commun contiendra les différentes fonctions additionnels aidant à l’optimisation du jeu au niveau du gameplay ainsi qu’au niveau design.

- Le dossier src contiendra aussi les fichiers nécessaires au lancement et a la bonne mise en route du jeu.

Et tout ce qui se trouvera en dehors du src seront des fichiers globaux comme le .gitignore ou le .env qui nous permettront une gestion de fichiers et de variables plus efficace.

## Algorithmes implémentant les trois fins de partie possibles.

### Première implémentation de fin de partie

    Au fur et à mesure de la partie, les cases se remplissent et dès qu’un des deux joueurs ne peut plus remplir une case la partie est fini

### Deuxième implémentation de fin de partie

    Il s’agit la de rejoindre les deux bords opposés de même couleur de la table de jeu afin de mettre fin à la partie, et donc si les deux bords de même couleur sont reliés de bout en bout par un joueur, on assistera à une fin de partie.

### Troisième implémentation de fin de partie

    A chaque tour de jeu on va vérifier à partir de la dernière case posée si cette case possède des voisins non-alliés, de même nous allons vérifier les cases adjacentes allié ou non, de ces mêmes cases. De même nous listerons les côtés existants et SI un des groupes voisins ne possède pas de côté alors le joueur courant gagne. Il s’agit là d’entourer une case adverse afin de mettre fin à la partie
