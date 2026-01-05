# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 12:43:16 2026

@author: Antoine Laldjee--Deroubaix & Arthur Peng
"""



#1 : case noire
#2 : case blanche

def init(n:int)->list:
    tableau = [[0 for _ in range(2*n)] for _ in range(2*n)]
    tableau[n-1][n-1], tableau[n][n] = 2, 2
    tableau[n][n-1], tableau[n-1][n] = 1, 1
    
    return tableau


tab = init(3)


def affichage(grille):
    """
    

    Parameters
    ----------
    grille : TYPE
        tableau de taille 2n.

    Returns
    -------
    None.

    """
    n = len(grille) // 2
    dico = {0:'.', 1:'o', 2:'x'}

    print("  ", end='')
    for k in range(2*n):
        print(k, end=' ')
    print()

    for i in range(2*n):
        print(i, end=' ')
        for j in range(2*n):
            print(dico[grille[i][j]], end=' ')
        print()

            
affichage(init(3))
#%% 
def est_sur_la_grille(i:int, j:int, n:int)->bool:
    """
    

    Parameters
    ----------
    i : int
        DESCRIPTION.
    j : int
        DESCRIPTION.
    n : int
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    if i >2*n -1 or j > 2*n -1 or i<0 or j<0:
        return False
    else :
        return True

print(est_sur_la_grille(3, 10, 5))
print(est_sur_la_grille(0, 7, 4))


#%% 4

def retourne_droite(grille:list, i:int, j:int, joueur:int)->list:
    """
    

    Parameters
    ----------
    grille : list
        DESCRIPTION.
    i : int
        DESCRIPTION.
    j : int
        DESCRIPTION.
    joueur : int
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    """
    n = len(grille) // 2
    if j == 2*n-1:
        return []
    elif grille[i][j+1] == 3 - joueur:
        for k in range (j+1, 2*n):
            if grille[i][k] == joueur:
                return [(i, l) for l in range(j+1, k)]
    return []
        
print(retourne_droite(init(4), 3, 2, 1))
 
#%%  
       
def retourne(grille, i, j, joueur):
    n = len(grille) // 2
    if j == 2*n-1:
        return []
    elif grille[i][j+1] == 3 - joueur:
        for k in range (j+1, 2*n):
            if grille[i][k] == joueur:
                return [(i, l) for l in range(j+1, k)]
    return []



for a in range(-1,1):
for b in range(-1,1)