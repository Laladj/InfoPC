# -*- coding: utf-8 -*-
"""
Créé le  Mon Sep 22 14:17:41 2025

Antoine Laldjee-Deroubaix, HX1


"""

def somme_max(A:list):
    m = len(A)
    n = len(A[0])
    somme = 0
    x, y= 0, 0 
    while x <= m-1 and y <= n-1:
        somme += A[x][y]
        if A[x+1][y]>=A[x][y+1]:
            
            somme += A[x+1][y]
            x = x+1
        else:
            somme += A[x][y+1]
            y += 1
    return somme


     
print(somme_max(A))

# %%


def somme_max_rec(A):
    n=len(A)
    m=len(A[0])
    def aux(i, j):
        # calcule la somme d'un chemin de (0,0) à (i,j)
        if i==0 and j==0:
            return A[0][0]
        if i==0 :
            return A[0][j] + aux(0,j-1)
        if j==0 :
            return A[i][0] + aux(i-1,0)
        return A[i][j]+ max(aux(i-1,j), aux(i,j-1))
    return aux(n-1, m-1)

A = [[2,8, 5, 4], [2, 9, 18, 2],[14,3, 9, 5], [12,92, 2, 1]]

print(somme_max_rec(A))


# %%

def somme_max_memo(A):1
    D={}
    def aux(i,j):
        if (i,j) in D :
            return D[(i,j)]
        elif i==0 and j==0:
            res = A[0][0]
        elif i==0 :
            res = A[0][j] + aux(0,j-1)
        elif j==0 :
            res= A[i][0] + aux(i-1,0)
        else:
            res = A[i][j]+ max(aux(i-1,j), aux(i,j-1))
        D[(i, j)] = res
        return res
    return aux(n-1, m-1)
            
       
#%%

def somme_max_tab(A):
    n = len[A]
    m = len[A[0]-1]
    w = [[0 for in range(m)] for in range (n)]
    def aux(i,j):
        w[0][0]= A[0][0]
        elif i==0 and j==0:
            res = A[0][0]
        elif i==0 :
            res = A[0][j] + aux(0,j-1)
        elif j==0 :
            res= A[i][0] + aux(i-1,0)
        else:
            res = A[i][j]+ max(aux(i-1,j), aux(i,j-1))
        D[(i, j)] = res
        return res
    return aux(n-1, m-1)
    







