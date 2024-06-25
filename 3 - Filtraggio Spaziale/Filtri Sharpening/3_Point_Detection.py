# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:25:46 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

''' POINT DETECTION
Filtraggio + Thresholding
- Soglia pari al 90% del livello di grigio più grande in val assoluto
-Troviamo una porosità in alto a destra
'''

x = np.float64(io.imread('turbina.jpg'))

#filtriamo prima con filtro lapliaciano
h = np.array([[-1,-1,-1],
              [-1,8,-1],
              [-1,-1,-1]])
y = ndi.correlate(x,h)

soglia = abs(np.max(y))*0.9
mask = y >soglia

plt.figure(); plt.imshow(mask, cmap='gray')

res = x*mask

plt.figure()
plt.subplot(131); plt.imshow(x, cmap='gray'); plt.title('Originale')
plt.subplot(132); plt.imshow(y, cmap='gray'); plt.title('Filtrato')
plt.subplot(133); plt.imshow(res, cmap='gray'); plt.title('Risultato')