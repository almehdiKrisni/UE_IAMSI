% Casse-tête logique

% Ensemble de prédicats
position(1..5). % Il y a 5 maisons
nationalite(britannique; suedois; danois; norvegien; allemand).
couleur(rouge; verte; blanche; jaune; bleue).
animal(chien; oiseaux; chats; chevaux; poissons).
boisson(the; cafe; lait; biere; eau).
cigarette(pallmall; dunhill; blend; bluemaster; princess).

% Contraites
% Chaque personne ne boit qu'une seule boisson distincte de celle des autres.
1 {boit(N, B) : boisson(B)} 1 :- nationalite(N).
:- boit(N1, B), boit(N2, B), boisson(B), nationalite(N1; N2), N1 != N2.

% Chaque personne possède un animal distinct de celui des autres.
1 {possede(N1, A) : animal(A)} 1 :- nationalite(N1).
:- possede(N1, A), possede(N2, A), animal(A), nationalite(N1; N2), N1 != N2.

% Chaque personne fume une marque de cigarette distincte de celle des autres.
1 {fume(N, C) : cigarette(C)} 1 :- nationalite(N).
:- fume(N1, C), fume(N2, C), cigarette(C), nationalite(N1; N2), N1 != N2.

% Chaque maison est de couleur différente des autres
1 {maison(X, C) : couleur(C)} 1 :- position(X).
:- maison(X1, C), maison(X2, C), couleur(C), position(X1; X2), X1 != X2.

% Chaque personne habite dans une maison différente de celle des autres
1 {habite(N, X) : position(X)} 1 :- nationalite(N).
:- habite(N1, X), habite(N2, X), position(X), nationalite(N1; N2), N1 != N2.

% Informations intiales
% Le Britannique vit dans la maison rouge.
habite(britannique, X) :- position(X), maison(X, rouge).

% Le Suédois garde un chien.
possede(suedois, chien).

% Le Danois boit du thé.
boit(danois, the).

% La maison verte est à gauche de la maison blanche.
maison(X1, verte) :- maison(X2, blanche), position(X1; X2), X1 == X2 - 1.

% Le propriétaire de la maison verte boit du café.
boit(N, cafe) :- nationalite(N), habite(N, X), position(X), maison(X, verte).

% La personne qui fume des Pall Mall possède des oiseaux.
possede(N, oiseaux) :- fume(N, pallmall), nationalite(N).

% Le propriétaire de la maison jaune fume des Dunhill.
fume(N, dunhill) :- habite(N, X), maison(X, jaune), nationalite(N), position(X).

% La personne qui vit dans la maison qui se trouve exactement au centre boit du lait.
boit(N, lait) :- habite(N, 3), nationalite(N).

% Le Norvégien vit dans la première maison.
habite(norvegien, 1).

% La personne qui fume des Blend vit à côté de celle qui possède des chats.
| X1 - X2 | == 1 :- fume(N1, blend), possede(N2, chats), habite(N1, X1), habite(N2, X2), nationalite(N1; N2), position(X1; X2).

% La personne qui possède des chevaux vit à côté du fumeur de Dunhill.
| X1 - X2 | == 1 :- possede(N1, chevaux), fume(N2, dunhill), habite(N1, X1), habite(N2, X2), nationalite(N1; N2), position(X1; X2).

% La personne qui fume des Bluemaster boit de la bière.
boit(N1, biere) :- fume(N1, bluemaster), nationalite(N).

% L’Allemand fume des Princess
fume(allemand, princess).

% Le Norvégien vit à côté de la maison bleue.
| X1 - X2 | == 1 :- habite(norvegien, X1), maison(X2, bleue), position(X1; X2).

% La personne qui fume des Blend a un voisin qui boit de l’eau.
| X1 - X2 | == 1 :- fume(N1, blend), boit(N2, eau), habite(N1, X1), habite(N2, X2), nationalite(N1; N2), position(X1; X2).


% On sélectionne les prédicats à afficher, soit qui possede quoi (on cherche les poissons).
#show possede/2.