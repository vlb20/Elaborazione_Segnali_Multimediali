# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:51:47 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

x = np.float32(io.imread("mammografia.jpg"))
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')
#y = K-1-x: NEGATIVO
y = 255 - x
plt.figure(2)
plt.imshow(y, clim=[0,255], cmap='gray')
