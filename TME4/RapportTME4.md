# Rapport TME4 IAMSI

Membres du binôme :
- KRISNI Almehdi (3800519)
- ARICHANDRA Santhos (3802651)

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
On obtient alors le système suivant avec 36 variables et 114 équations :
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

Il nous faudrait donc (ne! / (ne - 2)!), soit 6 jours pour que l'on puisse trouver une solution. On écrit maintenant un nouveau programme avec 3 équipes et 6 jours.
On obtient alors le système suivant avec 54 variables et 204 contraintes :
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

D'après Glucose, ce système est satisfiable. On obtient la solution suivante :

