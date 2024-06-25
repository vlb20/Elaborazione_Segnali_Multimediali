# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:25:58 2024

@author: vince
"""

# def deselect_bitplanes(x, index):
#     """
#     Ricostruzione immagine ponendo a zero i bit-plane fino all'i-esimo (dall'MSB to i) bit-plane indicato
#     Ritorna l'immagine modificata
#     """
#     x_mod = np.copy(x)
#     for i in range(index+1):
#         x_mod = bitset(x_mod, i, 0)
#     return x_mod

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

x = io.imread("frattale.jpg")

y1 = ML.deselect_bitplanes(x, 1)
y2 = ML.deselect_bitplanes(x, 2)
y3 = ML.deselect_bitplanes(x, 3)
y4 = ML.deselect_bitplanes(x, 4)
y5 = ML.deselect_bitplanes(x, 5)
y6 = ML.deselect_bitplanes(x, 6)
y7 = ML.deselect_bitplanes(x, 7)

plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')
plt.title("Originale")

plt.figure(2)
plt.imshow(y1, clim=None, cmap='gray')
plt.title("1 bit plane-azzerato")

plt.figure(3)
plt.imshow(y2, clim=None, cmap='gray')
plt.title("2 bit plane-azzerati")

plt.figure(4)
plt.imshow(y3, clim=None, cmap='gray')
plt.title("3 bit plane-azzerati")

plt.figure(5)
plt.imshow(y4, clim=None, cmap='gray')
plt.title("4 bit plane-azzerati")

plt.figure(6)
plt.imshow(y5, clim=None, cmap='gray')
plt.title("5 bit plane-azzerati")

plt.figure(7)
plt.imshow(y6, clim=None, cmap='gray')
plt.title("6 bit plane-azzerati")

plt.figure(8)
plt.imshow(y7, clim=None, cmap='gray')
plt.title("7 bit plane-azzerati")
