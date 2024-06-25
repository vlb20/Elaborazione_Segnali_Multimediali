# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:33:34 2024

@author: vince
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

x = np.float64(io.imread("quadrato.jpg"))

#FILTRI DI SOBEL
h1 = np.array([[-1,-1,-1],
               [2,2,2],
               [-1,-1,-1]])

h2 = np.array([[-1,-1,2],
               [-1,2,-1],
               [2,-1,-1]])

h3 = np.array([[-1,2,-1],
               [-1,2,-1],
               [-1,2,-1]])

h4 = np.array([[2,-1,-1],
               [-1,2,-1],
               [-1,-1,2]])

y1 = ndi.correlate(x,h1)
y2 = ndi.correlate(x,h2)
y3 = ndi.correlate(x,h3)
y4 = ndi.correlate(x,h4)

plt.figure(1); plt.imshow(x, clim=None,cmap='gray'); plt.title("Originale")
plt.figure(2); plt.imshow(y1, clim=None,cmap='gray'); plt.title("Filtrata con filtro orizzontale")
plt.figure(3); plt.imshow(y2, clim=None,cmap='gray'); plt.title("Filtrata con filtro obliquo")
plt.figure(4); plt.imshow(y3, clim=None,cmap='gray'); plt.title("Filtrata con filtro verticale")
plt.figure(5); plt.imshow(y4, clim=None,cmap='gray'); plt.title("Filtrata con filtro obliquo")

#Creiamo la matrice 3D lungo la terza direzione (profondità)
y5 = np.stack((y1,y2,y3,y4), axis=2)
y5 = np.max(y5, 2) #prendiamo il massimo lungo la terza direzione

plt.figure(6); plt.imshow(y5, clim=None, cmap='gray'); plt.title("line detection in tutte le direzioni")

soglia = 0.3 * np.max(y5)
mask = y5>soglia

plt.figure(7); plt.imshow(mask, clim=[0,1],cmap='gray'); plt.title("maschera")
