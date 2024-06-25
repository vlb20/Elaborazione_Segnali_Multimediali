# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:15:59 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

'''FILTRAGGIO NON LINEARE - FILTRO MEDIANO'''

x = np.float64(io.imread('circuito_rumoroso.jpg'))
y = ndi.generic_filter(x, np.median, (5,5))
#in alternativa y=ndi.median_filter(x, (5,5))
plt.figure()
plt.subplot(121); plt.imshow(x, clim=[0,255], cmap='gray'); plt.title("Originale")
plt.subplot(122); plt.imshow(y, clim=[0,255], cmap='gray'); plt.title("Filtro mediano")