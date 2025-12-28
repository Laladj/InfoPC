#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 21:03:05 2025

@author: Antoine Laldjee-Deroubaix


TD : 4 : Etude exacte des jeux


"""

g1 = {(1, 0): [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5)],
              (2, 1): [(1, 4), (1, 5), (1, 6)],
              (1, 1): [(2, 4), (2, 5), (2, 6)],
              (2, 2): [(1, 1), (1, 3), (1, 4), (1, 5)],
              (1, 3): [(2, 5), (2, 6), (2, 7)],
              (2, 3): [(1, 5), (1, 6), (1, 7)],
              (1, 4): [(2, 7), (2, 8)],
              (2, 4): [(1, 7), (1, 8)],
              (1, 5): [(2, 8)], 
              (2, 5): [(1, 8)],
              (1, 6): [(2, 5), (2, 7)], 
              (2, 6): [(1, 5), (1, 7)],
              (1, 7): [(2, 8)], 
              (2, 7): [(1, 8)],
              (1, 8): [], (2, 8): []
              }

import random as rd


#%% calcul du graphe opposé

def graphe_inverse(graphe:dict)->dict:
    inverse ={sommet : [] for sommet in graphe}
    for sommet in graphe:
        for voisin in graphe[sommet]:
            inverse[voisin].append(sommet)
    
    return inverse


g0 = {1: [2,4,6], 2: [1,4,5], 3:[4], 4:[5], 5: [], 6:[2]}

print(graphe_inverse(g0))

#%% etats finaux

def etats_finaux(g:dict, j:int)->dict:
    joueur = 3-j
    liste = []
    for sommet in g:
        if g[sommet] == [] and sommet[0] == joueur:
            liste.append(sommet)
            
    return liste

print(etats_finaux(g1, 1))
print(etats_finaux(g1, 2))


#%% degres sortants

def degres_sortants(g:dict)->dict:
    
    return {sommet:len(g[sommet]) for sommet in g}

print(degres_sortants(g1))


#%% attracteur 

def attracteur(arene:dict,joueur:int):
    """
    

    Parameters
    ----------
    arene : dict
        DESCRIPTION.
    joueur : int
        DESCRIPTION.

    Returns
    -------
    caclul de l'attracteur.

    """
    gInv = graphe_inverse(arene)
    F = etats_finaux(arene, joueur)
    d = degres_sortants(arene) #dictionnaire des degres sortants
    joueur = 3-joueur
    A = {} # attracteur : dictionnaire des positions gagnantes
    
    
    def parcours(s):
       if s not in A:
           A[s] = True
           if s in gInv:
               for u in gInv[s]:
                   if u[0] == joueur:  # Si u appartient à l'adversaire
                       parcours(u)
                   else:  # Si u appartient au joueur
                       d[u] -= 1
                       if d[u] == 0:
                           parcours(u)
   
    for s in F:
       parcours(s)
   
    return A

print(attracteur(g1, 1))
    
#complexite 


#%%jeu de nim 

def jeu_de_Nim(n:int, p:int)->dict:
    """
    
    Parameters
    ----------
    n : int
        batonnets.
    p : int
        batonnets pris par tour.
    Returns
    -------
    dict
        arene du jeu de Nim.
    """
    arene = {}
    def aux(etat): #couple (j,k):
        
        if etat in arene:  
            return
        
        joueurAdverse = etat[0]%2 +1 
        k = etat[1]
        
        if k == 0:
            arene[etat] = []  
            return  
            
        successeurs = []
        for i in range(1, min(p, k) + 1):
            successeur = (joueurAdverse, k - i)
            successeurs.append(successeur)
            aux(successeur)
    
        arene[etat] = successeurs
    
    aux((1,n))
    
    return arene

print(jeu_de_Nim(4,3))


#v 

graphe21Batonnets = jeu_de_Nim(21, 3)

att = attracteur(graphe21Batonnets, 1)

# pour le joueur 1, on remarque qu'il laisse un nombre d'allumettes congru
# a 1 modulo 4 : 1, 5, 9, 13, 17, 21 
# cela est bien conforme a la stratégie connue


#%% calcul d'une strategie gagnante


#i

def strategie(arene:dict, joueur:int)->dict:
    """
    

    Parameters
    ----------
    arene : dict
        DESCRIPTION.
    joueur : int
        DESCRIPTION.

    Returns
    -------
    dict
        DESCRIPTION.

    """
    gInv = graphe_inverse(arene)
    F = etats_finaux(arene, joueur)
    d = degres_sortants(arene) #dictionnaire des degres sortants
    joueur = 3-joueur
    A = {} # attracteur : dictionnaire des positions gagnantes
    
    
    def parcours(s):
       if s not in A:
           A[s] = True
           if s in gInv:
               for u in gInv[s]:
                   if u[0] == joueur:  # Si u appartient à l'adversaire
                       parcours(u)
                   else:  # Si u appartient au joueur
                       d[u] -= 1
                       if d[u] == 0:
                           parcours(u)
   
    for s in F:
       parcours(s)
   
    return A


        
        