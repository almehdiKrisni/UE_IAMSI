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
Il s'agit des méthodes codage et decodage du fichier *champ.py*.

## **Exercice 3**

### **Question 1**
Les méthodes *auMoinsUn* et *auPlusUn* sont implémentées dans le fichier code.

### **Question 3**
On met en place la méthode *generationCNF* allant écrire tout le système dans le fichier *champSys.cnf*.

On écrit un premier système avec 3 équipes et 4 jours. On obtient le système suivant :

