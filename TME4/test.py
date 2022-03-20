def codage(ne, nj, j, x, y):
    """ Retourne l'indice k de la variable propositionnelle vk correspondant.
        @param ne: int, nombre d'équipes participantes
        @param nj: int, nombre de jours de matchs maximum
        @param j: int, numéro du jour pour un match
        @param x: int, numéro de l'équipe à domicile
        @param y: int, numéro de l'équipe à l'extérieur
        @return k: int, indice de la variable vk correspondant
    """
    return j * ne**2 + x * ne + y + 1

def decodage(k, ne):
    """ Décode la valeur de l'indice k d'une variable vk et renvoie le jour j
        et les équipes x et y correspondant.
        @param k: int, indice de la variable vk
        @param ne: int, nombre d'équipes participantes
        @return j: int, numéro du jour du match
        @return x: int, numéro de l'équipe à domicile
        @return y: int, numéro de l'équipe à l'extérieur
    """
    j = ( k - 1 ) // ne**2
    x = ( ( k - 1 ) % ne**2 ) // ne
    y = ( k - 1 ) % ne
    return j, x, y


############## EXERCICE 3 - GENERATION D'UN PLANNING DE MATCHS ###############


# ----------------------  Contraintes de cardinalité ------------------------

def au_moins_un(vars):
    """ Renvoie une clause au format DIMACS traduisant la contrainte 'au moins
        une de ces variables est vraie'.
        @param vars: list(int), liste de variables
        @return clause: str, clause correspondant à la contrainte
    """
    return " " .join( str(i) for i in vars ) + " 0\n"

def au_plus_un(vars):
    """ Renvoie les clauses au format DIMACS traduisant la contrainte 'au plus
        une de ces variables est vraie' (encodage par paires).
        @param vars: list(int), liste de variables
        @return clause: str, clauses correspondant à la contrainte
    """
    clause = ""
    
    # Bouclage sur l'ensemble des couples de variables
    for i in range( len(vars) ):
        for j in range( i + 1, len(vars) ):
            clause += au_moins_un( [-vars[i], -vars[j]] )
            
    return clause


# ------------------------- Traduction du problème ---------------------------

def encoderC1(ne, nj):
    """ Contrainte 1: Chaque équipe ne peut jouer plus d'un match par jour.
        @param ne: int, nombre d'équipes participantes
        @param nj: int, nombre de jours de match maximum
        @return clause: str, clauses correspondant à la contrainte
    """
    clause = ""
    
    # Bouclage sur les équipes x et et les jours j
    for x in range(ne):
        for j in range(nj):
            # Liste des variables apparaissant dans la contrainte pour (x,j)
            vars = []
            for y in range(ne):
                if x != y:
                    vars.append(codage(ne, nj, j, x, y))
                    vars.append(codage(ne, nj, j, y, x))
            clause += au_plus_un(vars)
            
    return clause

def encoderC2(ne, nj):
    """ Contrainte 2: Sur le championnat, chaque équipe doit rencontrer l’
                      ensemble des autres équipes une fois exactement à
                      domicile et une fois exactement à l’extérieur.
        @param ne: int, nombre d'équipes participantes
        @param nj: int, nombre de jours de match maximum
        @return clause: str, clauses correspondant à la contrainte
    """
    clause = ""
    
    # Bouclage sur chaque paire d'équipes adverses (x,y)
    for x in range(ne):
        for y in range(ne):
            if x != y:
                # Liste des variables apparaissant dans la contrainte pour (x,y)
                vars = []
                for j in range(nj):
                    vars.append(codage(ne, nj, j, x, y))
                clause += au_plus_un(vars)
                clause += au_moins_un(vars)
    
    return clause

def encoder(ne, nj):
    """ Encode toutes les contraintes C1 et C2 pour ne et nj données.
        @param ne: int, nombre d'équipes participantes
        @param nj: int, nombre de jours de match maximum
        @return clause: str, clauses correspondant aux contraintes C1 et C2
    """
    clause = encoderC1(ne,nj) + encoderC2(ne,nj)
    nb_clauses = clause.count('\n')
    nb_vars = nj * ne**2
    
    return "p cnf {} {}\n".format(str(nb_vars),str(nb_clauses)) + clause

def genere_cnf(ne, nj):
    """ Génère un fichier cnf à partir de l'encodage avec ne et nj données.
        @param ne: int, nombre d'équipes participantes
        @param nj: int, nombre de jours de match maximum
    """
    with open('championnat.cnf', 'w') as file:
        file.write(encoder(ne,nj))

genere_cnf(3, 4)