# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:11:25 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

x = np.float64(io.imread("test.jpg"))

# FILTRO MEDIA ARITMETICA

#Definiamo la maschera (filtro) -> matrice k*k di "uni" /k^2
k = 3 # Dimensioni blocchetto
h = np.ones((k,k))/(k**2) #matrice k*k di "uni" e divido per k^2
y = ndi.correlate(x, h, mode='reflect') #estensione simmetrica ai bordi

plt.figure()
plt.subplot(121)
plt.imshow(x, clim=None, cmap='gray')
plt.title('originale')
plt.subplot(122)
plt.imshow(y, clim=None, cmap='gray')
plt.title('filtro media aritmetica')

#alternativamente filtro media aritmetica e filtro gaussiano
y1 = ndi.uniform_filter(x, 3, mode='reflect')
y2 = ndi.gaussian_filter(x, sigma=5) #più sigma è grande più assomiglia a un filtro uniforme

plt.figure()
plt.subplot(121); plt.imshow(y1, clim=None, cmap='gray'); plt.title("filtro media aritmetica")
plt.subplot(122); plt.imshow(y2, clim=None, cmap='gray'); plt.title("filtro gaussiano")

'''FILTRO DI SMOOTHING CON LA SEGUENTE MASCHERA:
      1 2 1
      2 4 2 /16
      1 2 1 
'''
mask = np.array([[1,2,1],
                 [2,4,2],
                 [1,2,1]])/16
y = ndi.correlate(x, mask, mode='reflect')
plt.figure()
plt.subplot(121); plt.imshow(x, clim=None, cmap='gray'); plt.title("originale");
plt.subplot(122); plt.imshow(y, clim=None, cmap='gray'); plt.title("filtro smoothing")

'''SMOOTHING SEGUITO DA THRESHOLDING
Filtro media spaziale -> sfoco l'immagine in modo da confondere
con lo sfondo oggetti piccoli di poco interesse ed enfatizzare
oggetti più grandi.

1. Filtro media aritmetica 15x15
2. Thresholding con soglia pari al 25% del valore massima
'''

sp = np.float64(io.imread("space.jpg"))
k1 = 15 #dimensioni blocchetto
h1 = np.ones((k1,k1))/(k1**2) #matrice k*k di uni e divido per k^2
y3 = ndi.correlate(sp, h1, mode='reflect')

plt.figure(1)
plt.imshow(sp, clim=None, cmap='gray')
plt.title("originale")
plt.figure(2)
plt.imshow(y3, clim=None, cmap='gray')
plt.title("filtrata con media")

# Threshold
maximum = np.max(y3)
maximum = maximum*0.25 #prendo il 25 percento

# Maschera
mask = y3 >= maximum

res = sp*mask

plt.figure(3)
plt.imshow(mask, clim=None, cmap='gray')
plt.title("maschera")

plt.figure(4)
plt.imshow(res, clim=None, cmap='gray')
plt.title("output")



