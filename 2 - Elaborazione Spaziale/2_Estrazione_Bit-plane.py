# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:17:31 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

x = io.imread('frattale.jpg')
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')
plt.title("Immagine originale")

from bitop import bitget
B = bitget(x, 7)         #estrazione bit-plane più significativo
plt.figure(2)
plt.imshow(B, clim=[0,1], cmap='gray') #visualizzazioe bit-plane
plt.title('bit-plane più significativo (7)')
B0 = bitget(x, 0)
plt.figure(3)
plt.imshow(B0, clim=[0,1], cmap='gray') #visualizzazioe bit-plane
plt.title('bit-plane meno significativo (0)')