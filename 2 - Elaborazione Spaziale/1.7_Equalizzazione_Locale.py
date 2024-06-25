# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:12:32 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

x = np.float32(io.imread('quadrato.tif'))

plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')
plt.title("Originale")

#Equalizzazione globale
from skimage.exposure import equalize_hist

y = equalize_hist(x)
y = 255*x
plt.figure(2)
plt.imshow(y, clim=None, cmap='gray')
plt.title("equalizzazione globale")

#Enhancement globale
y1 = ndi.generic_filter(x, ML.equalize_block, (3,3))
plt.figure(3)
plt.imshow(y1, clim=None, cmap='gray')
plt.title("equalizzazione globale")
