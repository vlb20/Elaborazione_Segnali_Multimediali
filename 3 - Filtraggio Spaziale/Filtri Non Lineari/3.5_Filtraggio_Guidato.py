# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:58:05 2024

@author: vince
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

plt.close('all')

'''Si vuole realizzare un filtraggio in cui 
  si trasferisce la struttura dei bordi da un’immagine (detta guida), g,
  alla sua mappa di segmentazione binaria, x.
'''

#NORMALIZZIAMO MASCHERA E GUIDA
g = np.float64(io.imread('guida.png')) / 255  # normalizzazione in [0,1]
x = np.float64(io.imread( 'mask.png')) / 255 
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(g, clim=[0, 1], cmap='gray')
plt.title('immagine guida');
plt.subplot(1,2,2)
plt.imshow(x, clim=[0, 1], cmap='gray')
plt.title('maschera binaria');

def filtro_guidato(x, g, B):
    #calcolo le immagini delle medie locali di x e g
    Med_x = ndi.uniform_filter(x, (B,B))
    Med_g = ndi.uniform_filter(g, (B,B))
    #Immagine varianze locali di g
    Var_g = ndi.generic_filter(g, np.var, (B,B))
    
    #Immagine delle correlazioni locali
    Corr_gx = ndi.uniform_filter(g*x, (B,B))
    
    #uscita del filtro
    eps = 2**(-60)
    a = (Corr_gx - Med_x*Med_g) / (Var_g + eps)
    b = Med_x - a*Med_g
    
    Med_a = ndi.uniform_filter(a, (B,B))
    Med_b = ndi.uniform_filter(b, (B,B))
    
    y = Med_a*g + Med_b
    return y

y = filtro_guidato(x, g, 10); 

plt.figure(2)
plt.imshow(y, clim=[0, 1], cmap='gray')
plt.title('maschera elaborata');

plt.figure(3)
plt.subplot(1,2,1)
plt.imshow(x*g, clim=[0, 1], cmap='gray')
plt.title('oggetto segmentato con la maschera binaria originale')
plt.subplot(1,2,2)
plt.imshow(y*g, clim=[0, 1], cmap='gray')
plt.title('oggetto segmentato con la maschera binaria elaborata')

plt.figure(4)
plt.subplot(2,2,1); plt.imshow(x[200:300,50:150], clim=[0, 1], cmap='gray'); plt.title('zoom di x'); 
plt.subplot(2,2,2); plt.imshow(y[200:300,50:150], clim=[0, 1], cmap='gray'); plt.title('zoom di y');
plt.subplot(2,2,3); plt.imshow(g[200:300,50:150]*x[200:300,50:150], clim=[0, 1], cmap='gray'); plt.title('zoom di gx');
plt.subplot(2,2,4); plt.imshow(g[200:300,50:150]*y[200:300,50:150], clim=[0, 1], cmap='gray'); plt.title('zoom di gy');

