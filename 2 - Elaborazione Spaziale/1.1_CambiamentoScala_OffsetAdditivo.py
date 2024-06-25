# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:37:39 2024

@author: vince
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

# OFFSET ADDITIVO
x = np.float32(io.imread('lena_bn.jpg'))
y1 = x+100 #traslo l'istogramma: più chiaro
y2 = x-100 
# CAMBIAMENTO DI SCALA
z1 = 2*x  #cambiamento di scala istogramma
z2 = 0.4*x 

plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')
plt.figure(2)
plt.subplot(1,2,1)
plt.imshow(y1, clim=[0,255], cmap='gray')
plt.title("x+100: chiaro")
plt.subplot(1,2,2)
plt.imshow(y2, clim=[0,255], cmap='gray')
plt.title("x-100: scuro")
plt.figure(3)
plt.subplot(1,2,1)
plt.imshow(z1, clim=[0,255], cmap='gray')
plt.title("2*x: valori grandi enfatizzati")
plt.subplot(1,2,2)
plt.imshow(z2, clim=[0,255], cmap='gray')
plt.title("0.4*x: valori grandi compressi")


