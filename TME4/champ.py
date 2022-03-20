# Fichier python concernant la mise en place des fichiers variables-contraintes de Championnat

# Partie 2 - Modélisation

# Question 2
def codage(ne, nj, j, x, y) :
    # Méthode de codage de la variable k en fonction de ne, nj, j, x et y
    return j * ne ** 2 + x * ne + y + 1

# Question 3
def decodage(k, ne) :
    # Méthode de décodage des variables j, x et y en fonction de k et ne
    # On utilise les multiplications divisions entières afin de retrouver les valeurs
    j = (k - 1) // ne ** 2
    x = ((k - 1) % ne ** 2) // ne
    y = (k - 1) % ne
    return j, x, y

## Partie 3 - Génération d'un planning de matchs

# Question 1 - Contraintes de cardinalité
def auMoinsUn(v) :
    # Création d'une clause au format DIMACS traduisant la contrainte "au moins un" sur les variables
    return " " .join(str(i) for i in v) + " 0\n"

def auPlusUn(v) :
    # Création des clauses au format DIMACS traduisant la contrainte "au plus un" sur les variables
    # On les compose en utilisant la méthode auMoinsUn
    c = ""

    # Création de tous les couples de variables possibles
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            c += auMoinsUn([-v[i], -v[j]])
            
    return c

# Question 2 - Traduction du problème
def encoderC1(ne, nj) :
    # La contrainte 1 stipule qu'une équipe ne peut jouer qu'un seul match par jour
    c = ""

    # On boucle sur les équipes x et les jours j
    for x in range(ne) :
        for j in range(nj) :

            # Liste des variables apparaissant dans la contrainte pour (x,j)
            v = []
            for y in range(ne) :
                if (x != y) :
                    v.append(codage(ne, nj, j, x, y))
                    v.append(codage(ne, nj, j, y, x))

            c += auPlusUn(v)
            
    # On retourne l'ensemble des clauses
    return c

def encoderC2(ne, nj):
    # La contrainte 2 stipule que chaque équipe doit faire un match avec toutes les autres
    # équipes (une fois à domicile et une fois à l'extérieur)
    c = ""
    
    # Bouclage sur chaque paire d'équipes adverses (x,y)
    for x in range(ne) :
        for y in range(ne) :
            if (x != y) :
                # Liste des variables apparaissant dans la contrainte pour (x,y)
                v = []

                for j in range(nj):
                    v.append(codage(ne, nj, j, x, y))

                c += auPlusUn(v)
                c += auMoinsUn(v)
    
    # On retourne l'ensemble des clauses
    return c

def encoder(ne, nj) :
    # On met en place une méthode allant permettre l'encodage de l'ensemble directement sur
    # un fichier
    c = encoderC1(ne, nj)
    c += encoderC2(ne, nj)

    # On compte le nombre de contraintes avec le nombre de retour à la ligne et le nombre de variables
    nbC = c.count('\n')
    nbV = nj * ne ** 2

    # On retourne le corps de contraintes
    return "p cnf " + str(nbV) + " " + str(nbC) +"\n" + c

# Question 3
def generationCNF(ne, nj) :
    # Méthode permet d'écrire toutes les contraintes dans le fichier champSys.cnf
    with open("champSys.cnf", 'w') as file :
        file.write(encoder(ne, nj))


# Partie EXEC
generationCNF(3, 6)