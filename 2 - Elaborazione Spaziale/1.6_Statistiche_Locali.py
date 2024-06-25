# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:38:03 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

x = np.float32(io.imread("filamento.jpg"))

#Vogliamo effettuare un'elaborazione (amplificazione del valore)
#solo dei pixel appartenenti alle aree scure, che abbiano basso
#contrasto, ma non nelle regioni piatte

#Un pixel VIENE ELABORATO SE:
# luminosità media locale < luminosità media globale
# dev. std. locale bassa ma non troppo (aree omogenee)

#immagine delle medie locali
MED = ndi.generic_filter(x, np.mean, (3,3))
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(MED, clim=None, cmap='gray')
#immagine delle deviazioni standard
DEV = ndi.generic_filter(x, np.std, (3,3))
plt.subplot(1,2,2)
plt.imshow(DEV, clim=None, cmap='gray')

k0 = 0.4
k1 = 0.02
k2 = 0.4

#Calcolo la media e dev.std globali
glob_mean = np.mean(x)
glob_std = np.std(x)
mask = (MED<=0.4*glob_mean) & (DEV<=0.4*glob_std) & (DEV>=0.02*glob_std)

plt.figure(2)
plt.imshow(mask, clim=None, cmap='gray')

y = x*mask*3 + x #applico l'elaborazione + immagine originale
plt.figure(3)
plt.imshow(y, clim=None, cmap='gray') 