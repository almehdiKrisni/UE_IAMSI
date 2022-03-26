% Jeu des reines

% Il faut poser n reines sur l'échiquier.
#const n = 8.
valideReine(1..n).
1 { reine(X, Y) : valideReine(X) } 1 :- valideReine(Y).

% Contrainte de dimension.
:- reine(X, Y), X > 8, X < 1, Y > 8, Y < 1.

% Contrainte sur les lignes.
:- reine(X, Y), reine(X, YY), Y != YY.

% Contrainte sur les colonnes.
:- reine(X, Y), reine(XX, Y), X != XX.

% Contrainte sur les diagonales.
:- reine(X, Y), reine(XX, YY), Y < YY, |X - XX| == YY - Y.

% Cas où une reine se trouve forcément en (1,1).
reine(1,1).
