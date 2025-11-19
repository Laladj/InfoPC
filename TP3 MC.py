#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 09:56:50 2025

@author: Antoine Laldjee-Deroubaix

Methode monte carlo pour un titrage
"""

import numpy as np
import numpy.random as rd

import matplotlib.pyplot as plt

N= 100000

############## Les volumes sont indiques en mL,les concentrations en mol/L

Cthio = 0.050
u_Cthio = 5e-4

Cag = 0.10
u_Cag = 0.001

Veq = 8.9
u_Veq = 0.05

VO = 10
u_VO = 0.040

V1 = 20
u_V1 = 0.06

Cthio_sim = Cthio + u_Cthio*rd.uniform(-1, 1, N)
Cag_sim = Cag + u_Cag*rd.uniform(-1, 1, N)
Veq_sim = Veq + u_Veq*rd.uniform(-1, 1, N)
VO_sim = VO + u_VO*rd.uniform(-1, 1, N)
V1_sim = V1 + u_V1*rd.uniform(-1, 1, N)

Cphi_sim = (Cag_sim*V1_sim- Cthio_sim*Veq_sim)/VO_sim



u_Cphi = np.std(Cphi_sim ,ddof =1) 
print('u_Cphi=', u_Cphi, 'mol L-1')