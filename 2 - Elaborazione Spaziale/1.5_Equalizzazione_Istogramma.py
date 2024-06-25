# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:03:51 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

x = np.float32(io.imread('marte.jpg'))
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')
plt.figure(2)
plt.hist(x.flatten(), 256)


#Equalizzazione Istogramma
from skimage.exposure import equalize_hist
y = equalize_hist(x) #l'output è nel range [0,1]
y = 255*y            #lo convertiamo nel range [0, 255]

plt.figure(3)
plt.imshow(y, clim=[0,255], cmap='gray')
plt.figure(4)
plt.hist(y.flatten(), 256)
