# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:55:01 2024

@author: vince
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
plt.close('all')

def enhanc(x, mask, k):
    # maschera del filtro
    a = 0.073
    b = 0.177
    h = np.array([[a,b,a],
                  [b,0,b],
                  [a,b,a]])
    
    #filtraggio dei pixel selezionati dalla maschera
    x = x*mask #sto mantenendo solo i pixel corrisponendi alle parti danneggiate (mask=1)
    for i in range(k):
        y = ndi.correlate(x, h) #filtro solo immagine con parti danneggiate
        
        #LA NUOVA IMMAGINE coincide ovunque con x originale tranne per la parte danneggiata che coincide con la filtrata
        x = (1-mask)*y + mask*x #aggiorno solo i pixel selezionati dalla maschera
    
    return x

x = np.float64(io.imread('bebe.jpg'))
mask = io.imread('mask.bmp')>0 #carico la maschera e la trasformo in binaria
#Impostiamo a 1 (vero) i pixel danneggiati e 0 (falso) quelle non danneggiate

plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')
plt.title('Immagine originale')

plt.figure(2)
plt.imshow(mask, clim=[0,1], cmap='gray')
plt.title('maschera')

# enhancement locale
list_k = [10, 50, 100]
for k in list_k:
   y = enhanc(x, mask, k);
   plt.figure()
   plt.imshow(y, clim=[0,255], cmap='gray')
   plt.title('enhancement con k = %d iterazioni' % k)

plt.show()
