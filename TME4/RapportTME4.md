# Rapport TME4 IAMSI

Membres du binôme :
- KRISNI Almehdi (3800519)
- ARICHANDRA Santhos (3802651)

## Notes importantes
Devant passer par une machine Virtuelle afin d'utiliser Glucose, nous avons effectué certains des tests en utilisant une VM Linux. Devant transférer à chaque fois les fichiers via GitHub, nous avons décidé par la suite d'utiliser la libraire Pycosat afin d'effectuer directment les résolutions de système en Python pour que la tâche soit moins pénible.

## **Exercice 1**

Pour la première théorie, on obtient le résultat suivant avec Glucose :<br/>
s SATISFIABLE
v 1 -2 -3 4 -5 -6 7 -8 0

Pour la deuxième théorie, on obtient le résultat suivant :<br/>
s SATISFIABLE
v 1 -2 -3 4 5 -6 -7 -8 -9 10 -11 12 -13 -14 -15 -16 0

On vérifie que la formule F de l'exercice 2 est bien insatisfiable. On obtient le résultat suivant :<br/>
s UNSATISFIABLE

## **Exercice 2**

Afin de coder les différentes variables et contraintes du sujet, on décide de mettre en place un ficher allant réaliser des opérations d'écriture de fichier lors de son exécution.

Dans le fichier champ.py, on retrouve les méthodes codage et decodage permettant de transformer les variables obtenues.

### **Question 1**
Les jours étant compris dans l'ensemble [0, nj - 1], les équipes dans l'ensemble [0, ne - 1], il existe donc (nj * ne * (ne - 1)) combinaisons, donc de variables propositionnelles.

On (ne * (ne - 1)) puisqu'une équipe ne peut pas jouer contre elle-même.

### **Question 2 et 3**
Il s'agit des méthodes codage et decodage du fichier *champ.py*. Voir les commentaires pour plus de précisions.

## **Exercice 3**

### **Question 1**
Les méthodes *auMoinsUn* et *auPlusUn* sont implémentées dans le fichier code. Voir les commentaires pour plus de précisions.

### **Question 3**
On met en place la méthode *generationCNF* allant écrire tout le système dans le fichier *champSys.cnf*.

On écrit un premier système avec 3 équipes et 4 jours. 
On obtient alors le système suivant avec 36 variables et 114 équations :<br/>
-2 -4 0
-2 -3 0
-2 -7 0
-4 -3 0
-4 -7 0
...
-8 -35 0
-17 -26 0
-17 -35 0
-26 -35 0
8 17 26 35 0

Ce système est considéré comme insatisfiable d'après Glucose. On en déduit que les contraintes de l'énoncé ne sont pas suffisantes.

En regardant de plus près le problème, on se rend compte que pour 3 équipes, chacune d'entre elles devra en disputer exactement 4, donc 1 par match jour. Or, il ne peut y avoir qu'un seul match par jour puisqu'à chaque journée, deux équipes s'affrontent et une reste sans rencontre.

Il nous faudrait donc que le nombre minimal de jours soit de (ne! / (ne - 2)!) jours, soit 6 jours pour que l'on puisse trouver une solution. On écrit maintenant un nouveau programme avec 3 équipes et 6 jours.
On obtient alors le système suivant avec 54 variables et 204 contraintes :<br/>
-2 -4 0
-2 -3 0
-2 -7 0
-4 -3 0
-4 -7 0
-3 -7 0
...
-26 -53 0
-35 -44 0
-35 -53 0
-44 -53 0
8 17 26 35 44 53 0

D'après Glucose, ce système est satisfiable. On obtient la solution suivante :<br/>
v -1 -2 -3 4 -5 -6 -7 -8 -9 -10 11 -12 -13 -14 -15 -16 -17 -18 -19 -20 21 -22 -23 -24 -25 -26 -27 -28 -29 -30 -31 -32 33 -34 -35 -36 -37 -38 -39 -40 -41 -42 43 -44 -45 -46 -47 -48 -49 -50 -51 -52 53 0

### **Question 4 et 5**
On crée la méthode *decoder* permettant à partir d'un fichier .cnf d'obtenir le planning des matchs à partir d'une base de noms d'équipes lorsqu'elle est passée en paramètre. On crée également une autre méthode permettant d'obtenir des affiches de planning plus compréhensible.

On obtient par exemple, pour 3 équipes et 6 jours :<br/>
Jour 1<br/>
('Chelsea', 'PSG')<br/>
Jour 2<br/>
('Chelsea', 'RealMadrid')<br/>
Jour 3<br/>
('PSG', 'Chelsea')<br/>
Jour 4<br/>
('RealMadrid', 'Chelsea')<br/>
Jour 5<br/>
('RealMadrid', 'PSG')<br/>
Jour 6<br/>
('PSG', 'RealMadrid')<br/>

## **Exercice 4**
On cherche dans cette partie à optimiser le nombre de jours minimal afin de rendre un système de contraintes avec un nombre d'équipes réalisable.

On obtient les résultats suivants :

Pour 3 équipes, il faut au moins 6 jours.
Pour 4 équipes, il faut au moins 6 jours.

Pour une certaine raison, le code ne souhaite pas effectuer la recherche pour 5 équipes et plus puisqu'il crash en permanence.

