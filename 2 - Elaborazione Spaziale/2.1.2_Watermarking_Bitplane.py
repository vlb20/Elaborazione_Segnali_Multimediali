# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:41:46 2024

@author: vince
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

#Inseriamo un watermark y nel bitplane (index) dell'immagine x

x = np.fromfile("lena.y", np.uint8)
x = np.reshape(x, (512,512))

y = np.fromfile("marchio.y", np.uint8).T #ne faccio il trasposto
y = np.reshape(y, (350,350))


plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(x, clim=None, cmap='gray')
plt.title("immagine originale")
plt.subplot(1,2,2)
plt.imshow(y, clim=None, cmap='gray')
plt.title("marchio")

dim_y = 350

#Se dim_y < dim_x allora inserisco in alto a sinsistra il watermark
x_mod = np.copy(x)
from bitop import bitset
x_mod[:dim_y, :dim_y] = bitset(x[:dim_y, :dim_y], 4, y)
plt.figure(2)
plt.imshow(x_mod, cmap='gray')
