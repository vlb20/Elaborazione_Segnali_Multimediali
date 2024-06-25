# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:50:03 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

'''EDGE DETECTION BASATA SUL GRADIENTE'''

x = np.fromfile("house.y", np.uint8)
x = np.reshape(x, (512,512))
x = np.float64(x)


#Filtri di Sobel (orizzontale e verticale)
h1 = np.array([[-1,-2,-1],
               [0,0,0],
               [1,2,1]])

h2 = np.array([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])

y1 = ndi.correlate(x,h1)
y2 = ndi.correlate(x,h2)

#GRADIENTE: eleviamo al quadrato le immagini -> sommiamo -> radice
grad = np.sqrt(y1**2 + y2**2)

plt.figure(1); plt.imshow(x, cmap='gray'); plt.title("Originale")
plt.figure(2); plt.imshow(y1, cmap='gray'); plt.title("Sobel orizzontale")
plt.figure(3); plt.imshow(y2, cmap='gray'); plt.title("Sobel verticale")
plt.figure(4); plt.imshow(grad, cmap='gray'); plt.title("Edge Detection - Gradiente")

T = 1.5*np.mean(grad) #150% della media del gradiente

mask = grad>T
plt.figure(5); plt.imshow(mask, clim=[0,1], cmap='gray'); plt.title("Maschera")

'''ANGIOGRAMMA

SMOOTHING + EDGE DETECTION
'''

x = np.float64(io.imread("angiogramma.jpg"))

plt.figure(); plt.imshow(x, cmap='gray'); plt.title("Pre-Smoothing")
#filtro gaussiano -> facciamo uno smoothing
sigma = 2.0
x = ndi.gaussian_filter(x, (sigma,sigma))

#Filtri di sobel direzionali
h1 = np.array([[-1,-2,-1],
               [0,0,0],
               [1,2,1]])

h2 = np.array([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])

y1 = ndi.correlate(x,h1)
y2 = ndi.correlate(x,h2)

grad = np.sqrt(y1**2 + y2**2)

plt.figure(1); plt.imshow(x, cmap='gray'); plt.title("Post-Smoothing")
plt.figure(2); plt.imshow(y1, cmap='gray'); plt.title("Sobel orizzontale")
plt.figure(3); plt.imshow(y2, cmap='gray'); plt.title("Sobel verticale")
plt.figure(4); plt.imshow(grad, cmap='gray'); plt.title("Edge Detection - Gradiente")

T = 1.5*np.mean(grad) #150% della media del gradiente

mask = grad>T
plt.figure(5); plt.imshow(mask, clim=[0,1], cmap='gray'); plt.title("Maschera")