% Solveur Sudoku

% Génération de toutes les grilles possibles, sans contraintes
% On crée les différentes valeurs et les différentes positions

valeur(1..9). % Différentes valeurs possibles
pos(0..8). % Différentes positions X ou Y possibles

% Il ne peut y avoir qu'une seule valeur par case.
1 {case(X, Y, Z) : valeur(Z)} 1 :- pos(X), pos(Y).

% Création de contraintes (à mettre en commentaire).
% case(1,0,8).
% case(0,1,7).

% Contrainte 1 - Pas deux fois le même chiffre sur une ligne.
:- case(X, Y, Z), case(X, YY, Z), Y != YY, pos(X), pos(Y), pos(YY), valeur(Z).

% Contrainte 2 - Pas deux fois le même chiffre sur une colonne.
:- case(X, Y, Z), case(XX, Y, Z), X != XX, pos(X), pos(XX), pos(Y), valeur(Z).

% Contrainte 3 - Pas deux fois le même chiffre dans la même sous-grille.
:- case(X,Y,Z), case(XX, YY, Z), X/3 == XX/3, Y/3 == YY/3, X!= XX, Y != YY, pos(X), pos(XX), pos(Y), pos(YY), valeur(Z).

% Contraintes grille TME
case(0,1,7).
case(0,3,6).
case(0,5,3).
case(0,7,1).
case(0,8,4).
case(1,0,8).
case(1,4,9).
case(2,1,6).
case(2,2,3).
case(2,3,2).
case(2,4,1).
case(2,6,8).
case(3,4,3).
case(3,7,5).
case(3,8,9).
case(4,0,6).
case(4,3,9).
case(4,6,4).
case(4,8,1).
case(5,0,9).
case(5,1,2).
case(5,3,4).
case(5,5,1).
case(5,8,8).
case(6,1,5).
case(6,3,8).
case(6,8,3).
case(7,0,4).
case(7,2,1).
case(7,3,3).
case(7,4,6).
case(7,5,2).
case(7,6,7).
case(7,7,8).
case(8,0,3).
case(8,2,6).
case(8,3,1).
case(8,6,9).
case(8,8,2).