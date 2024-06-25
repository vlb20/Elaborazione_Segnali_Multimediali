# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:37:39 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML

x = np.float32(io.imread("spettro.jpg"))

#Operazione Logaritmo per migliorare il contrasto nelle zone scuro
y = np.log(x+1)
y = ML.fshs(y, 256)
plt.figure(1)
plt.subplot(1,2,1)
#FACCIAMO IL CONTRAST STRETCH DOPO UNA OPERAZIONE NON LINEARE
plt.imshow(x, clim=None, cmap='gray')
plt.title("Immagine Originale")
plt.subplot(1,2,2)
plt.imshow(y, clim=None, cmap='gray')
plt.title("Operazione Logaritmo")

##########################################


x1 = np.float32(io.imread("vista_aerea.jpg"))
#Trasformata Potenza
gamma1 = 3
y1 = x1**gamma1
y1 = ML.fshs(y1, 256)
plt.figure(2)
plt.subplot(1,2,1)
plt.imshow(x1, clim=None, cmap='gray')
plt.title("Originale")
plt.subplot(1,2,2)
plt.imshow(y1, clim=None, cmap='gray')
plt.title("Potenza con gamma=3")

x2 = np.float32(io.imread("spina_dorsale.jpg"))
#Trasformata Potenza
gamma2 = 0.3
y2 = x2**gamma2
y2 = ML.fshs(y2, 256)
plt.figure(3)
plt.subplot(1,2,1)
plt.imshow(x2, clim=None, cmap='gray')
plt.title("Originale")
plt.subplot(1,2,2)
plt.imshow(y2, clim=None, cmap='gray')
plt.title("Potenza con gamma=0.3")



