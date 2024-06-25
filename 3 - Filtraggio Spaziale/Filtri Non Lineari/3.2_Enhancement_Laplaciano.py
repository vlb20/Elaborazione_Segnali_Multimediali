# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:47:16 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

x = np.float64(io.imread('luna.jpg'))

#Laplaciano
h = np.array([[0,0,1,0,0],
              [0,0,0,0,0],
              [1,0,-4,0,1],
              [0,0,0,0,0],
              [0,0,1,0,0]])
y = ndi.correlate(x,h)

y_enh = x-y
plt.figure(1); plt.imshow(y_enh, cmap='gray')