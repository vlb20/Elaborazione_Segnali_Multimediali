# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:18:26 2024

@author: vince
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

# FILTRO LAPLACIANO
x = np.float64(io.imread("luna.jpg"))

h = np.array([[0,1,0],
              [1,-4,1],
              [0,1,0]])

y = ndi.correlate(x,h)

#Enhancement Luna
y2 = x - y
#equivalentemente 
# h = np.array([[0,1,0],
#              [1,-5,1],
#              [0,1,0]])
# z = ndi.correlate(x,h)

plt.figure()
plt.subplot(131); plt.imshow(x, cmap='gray'); plt.title("Originale")
plt.subplot(132); plt.imshow(y, cmap='gray'); plt.title("Filtro Laplaciano")
plt.subplot(133); plt.imshow(y2, cmap='gray'); plt.title("Enhancement")
