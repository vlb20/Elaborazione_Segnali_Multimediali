# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:20:30 2024

@author: vince
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

plt.close('all')
x = np.float64(io.imread('retina.tif')) / 255

plt.figure(1)
plt.imshow(x)
plt.title('immagine della retina');

def segmenta(x):
    G = x[:,:,1] #banda verde
    
    #creazione maschere
    K = 7
    mask1 = np.zeros((K,K))
    mask1[K//2: K//2+1] = 1
    mask2 = mask1.T #trasposta
    mask3 = np.eye(K)
    mask4 = mask3.T
    
    masks = np.stack((mask1,mask2,mask3,mask4), 0)
    
    #maschere per i bianchi
    masks_bianco = masks / np.sum(masks, (1,2), keepdims=True)
    
    #maschere per i neri
    masks_nero   = (1-masks) / np.sum((1-masks), (1,2), keepdims=True) 
    
    #calcolo delle medie
    M,N = G.shape
    y = np.zeros((M,N,4))
    for i in range(4):
        y[:,:,i] = ndi.correlate(G, masks_bianco[i] - masks_nero[i])
        
    #selezione del minimo
    y = np.min(y,2)
    
    #thresholding
    y = y < -5/255
    
    #eliminiamo il cerchio esterno che limita la retina
    j,i = np.meshgrid(np.arange(N)-N/2, np.arange(M)-M/2)
    m = (j**2 + i**2) < 0.2*N*M
    y = y*m
    return y

y = segmenta(x)
plt.figure(2)
plt.imshow(y, clim=[0,1], cmap='gray')
plt.title('risultato');