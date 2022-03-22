# Rapport TME 5 et 6 - IAMSI

Membres du binôme :
- KRISNI Almehdi
- ARICHANDRA Santhos

### Exercice 1 - Premiers pas en ASP

Afin de se familiariser avec l'environnement de Clingo, on réalise quelques tests sur les différents programmes fournis par l'énoncé du TME.
On affiche le ou les ensembles-réponses (answer sets) de chaque programme.

Programme 1 :
* conges temps_libre sortie_cine

Programme 2 :
* q

Programme 3 :
* p r
* q r

Programme 4 :
* p r

D'après Clingo, tous les programmes sont satisfiables et disposent donc d'au moins un answer set.

### Exercice 2 - Problème des 8-reines

Le jeu des reines consiste à placer 8 reines sur un plateau de jeu de 8x8 cases, et une reine par colonne.
Il existe différentes contraintes au sein du jeu puisqu'il est interdit de placer 2 reines sur la même ligne, colonne ou diagonale.

On écrit toutes ces contraintes dans le fichier 'Exercice2/reines.lp' puis on tente de résoudre le programme grâce à Clingo.

Une des solutions réalisable est :
valideReine(1) valideReine(2) valideReine(3) valideReine(4) valideReine(5) valideReine(6) valideReine(7) valideReine(8) 
reine(1,3) reine(2,5) reine(3,8) reine(4,4) reine(5,1) reine(6,7) reine(7,2) reine(8,6)

Le prédicat reine(X, Y) signifique qu'une reine se trouve à la position (X, Y) dans la solution et le prédicat valideReine(X) signifie que la reine de la colonne X a été placée sur l'échiquier.

On essaye maintenant de trouver une solution au jeu avec une reine forcément placée sur la case (1,1). On doit donc ajouter au système le prédicat reine(1, 1) et l'exécuter avec Clingo.
On obtient alors 4 solutions au problème. On affiche uniquement les prédicats 'reine' de la solution afin de faciliter la compréhension.
Les solutions obtenues sont :
* reine(1,1) reine(2,7) reine(3,5) reine(4,8) reine(5,2) reine(6,4) reine(7,6) reine(8,3)
* reine(1,1) reine(2,6) reine(3,8) reine(4,3) reine(5,7) reine(6,4) reine(7,2) reine(8,5)
* reine(1,1) reine(2,5) reine(3,8) reine(4,6) reine(5,3) reine(6,7) reine(7,2) reine(8,4)
* reine(1,1) reine(2,7) reine(3,4) reine(4,6) reine(5,8) reine(6,2) reine(7,5) reine(8,3)
