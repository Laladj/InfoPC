#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 09:06:00 2025

@author: antoine Laldjee-Deroubaix

DM2 
"""

#%% 1. Problème d'étagères

# =============================================================================
# après calcul, on dénombre un total de (n^3 + 3n² - 4n)/6 additions pour
# determiner la somme de tous les couples
# 
# On a donc une complexité en O(n³): quadratique
#     
# 2. Equation de Bellman
# 
# on a lequation suivante : 
#     S(i,j ) = S(i, j-1) + n(i) Si j >= i
#     S(i,i) = a i 
#     
# On definit donc une case du tableau seulement à partir de sa case de gauche
# 
# =============================================================================

    
def sommes_de_tranches(serie_nombres:list)->list:
    """
    

    Parameters
    ----------
    serie_nombres : liste d'entiers
        DESCRIPTION.

    Returns
    -------
    liste de n listes de taille n
        DESCRIPTION.

    """
    n = len(serie_nombres)
    tableau = [[0 for i in range(n)] for y in range(n)]
    
    for i in range(n):
        tableau[i][i] = serie_nombre[i]
        
    #en utilisant l'equation de Bellman
    for i in range(n):
        for j in range(i,n):
            tableau[i][j] = tableau[i][j-1]+serie_nombres[j]
            
    return tableau

serie_nombre = [x for x in range(0,10)]

tableau = sommes_de_tranches(serie_nombre)  

# =============================================================================
# [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
# [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
# [0, 0, 2, 5, 9, 14, 20, 27, 35, 44]
# [0, 0, 0, 3, 7, 12, 18, 25, 33, 42]
# [0, 0, 0, 0, 4, 9, 15, 22, 30, 39]
# [0, 0, 0, 0, 0, 5, 11, 18, 26, 35]
# [0, 0, 0, 0, 0, 0, 6, 13, 21, 30]
# [0, 0, 0, 0, 0, 0, 0, 7, 15, 24]
# [0, 0, 0, 0, 0, 0, 0, 0, 8, 17]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 9]
# On obtient bien le résultat escompté 
# =============================================================================

#%% 1.2 Etagère de hauteur minimale:
def hauteurs_de_rayon_minimales(bibliotheque:list,L:int)->dict:
    """
    

    Parameters
    ----------
    bibliotheque : liste de tuples 
        premier élément : lk 
    L : entier naturel non nul
        DESCRIPTION.

    Returns
    -------
    None.

    """
    n =len(bibliotheque)
    output = {}
    largeurs = [bibliotheque[i][0] for i in range(len(bibliotheque))]
    hauteurs = [bibliotheque[i][1] for i in range(len(bibliotheque))]
    tableauSommes = sommes_de_tranches(largeurs)
    
    #implémentation du cas de base : 
    for j in range(n):
        for i in range(j+1):
            if tableauSommes[i][j]<= L:
                output[(i,j)] = max(hauteurs[i:j+1])
            else:
                output[(i,j)] = float('inf')
    return output
B1 = [ (3, 5), (3,7), (2,9), (3, 3), (2, 10 )]

print(hauteurs_de_rayon_minimales(B1, 3))
#on ne dispose pas de la valeur de L prise pour tester la fonction

#5

