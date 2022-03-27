% Coloration de graphes

% Création du graphe
% Gestion du nombre de noeuds
noeud(1..7).

% Gestion du nombre de couleurs à utiliser
#const n = 4.
couleur(1..n).

% Il est impossible de générer les arêtes aléatoirement. On doit les ajouter à la main.
% Génération des arêtes et des arêtes inverses (pas de sens de circulation dans le graphe)
% Pour la numération, on commence du plus en haut à gauche au plus en bas à droite.
arete(1,2).
arete(1,3).
arete(1,5).
arete(2,3).
arete(2,4).
arete(2,6).
arete(3,4).
arete(3,5).
arete(3,6).
arete(4,5).
arete(4,6).
arete(5,6).
arete(5,7).
arete(6,7).
arete(Y,X) :- arete(X,Y). % Arêtes inverses

% Contraintes
% Un noeud ne peut avoir qu'une seule coloration
1 {coloration(N, C) : couleur(C)} 1 :- noeud(N).

% Deux noeuds adjacents ne peuvent pas avoir la même coloration
:- coloration(N1, C), coloration(N2, C), noeud(N1), noeud(N2), couleur(C), N1 != N2, arete(N1, N2).