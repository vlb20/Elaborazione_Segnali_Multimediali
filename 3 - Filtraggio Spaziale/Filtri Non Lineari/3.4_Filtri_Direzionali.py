# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:14:56 2024

@author: vince
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi


plt.close('all')

x = np.fromfile('zebre.y', np.uint8)
x = np.reshape(x, [321, 481])

plt.figure(1); plt.imshow(x, clim=[0,255], cmap='gray'); plt.title('Originale')

#Generazione immagine rumorosa
M,N = x.shape
n_std = 25
noisy = x + n_std*np.random.randn(M,N)
plt.figure(2); plt.imshow(noisy, clim=[0,255], cmap='gray'); plt.title('Rumorosa')

#FILTRO MEDIA ARITMETICA
y = ndi.uniform_filter(noisy, (5,5))

mse = np.mean((x-y)**2)
psnr = 10*np.log10((255*2)/mse)
plt.figure(3); plt.imshow(y, clim=[0,255], cmap='gray'); plt.title('Risulatato con filtro lineare (psnr:%5f) ' % psnr)

#CREAZIONE MASCHERE
K = 9; S=1
mask3 = np.triu(np.ones((K,K)), k=-S) - np.triu(np.ones((K,K)), k=+S+1) 
'''
triu matrice triangolare superiore partendo dalla diagonale subito sotto alla principale (k=-1) a cui sottraiamo la stessa ma partendo da 
diagonale sopra di 2 alla principale(k=S+1=2)
'''
mask1 = mask3[:,::-1] #flip sinistra-destra (righe uguali, colonne inverse)

mask2 = np.zeros((K,K)) #matrice di zeri
mask2[K//2-S: K//2+S+1] = 1 #pongo a 1 le righe selezionate (3-4-5)

mask4 = mask2.T #trasposta

masks = np.stack((mask1,mask2,mask3,mask4), 0)
masks = masks>0 #converto le maschere in booleani

plt.figure(4)
plt.subplot(1,4,1)
plt.imshow(masks[0], clim=[0,1], cmap='gray')
plt.subplot(1,4,2)
plt.imshow(masks[1], clim=[0,1], cmap='gray')
plt.subplot(1,4,3)
plt.imshow(masks[2], clim=[0,1], cmap='gray')
plt.subplot(1,4,4)
plt.imshow(masks[3], clim=[0,1], cmap='gray')

#funzione da applicare ad ogni blocco
def fun_blk(blk):
    #Valutazione delle varianze
    K,M,N = masks.shape
    blk = blk.reshape([M,N]) #vector->matrix
    
    vet_vars = np.zeros(K) #vettore delle varianze
    for k in range(K):
        #calcolo la varianza locale usando le 4 maschere (considero solo i pixel selezionati)
        vet_vars[k] = np.var(blk[masks[k]])
        
    #valutazione delle maschere a minima varianza
    idx = np.argmin(vet_vars) #prendo l'indice della maschera a varianza minima
    
    #Filtraggio del pixel corrispondene alla varianza minima con pesi tutti uguali
    value = np.mean(blk[masks[idx]])
    return value

y = ndi.generic_filter(noisy, fun_blk, (K,K))

#valutazione psnr
mse = np.mean((x-y)**2)
psnr = 10*np.log10((255**2)/mse)

plt.figure(5)
plt.imshow(y, clim=[0,255], cmap='gray')
plt.title('Risulatato con filtro non-lineare (psnr:%5f)' % psnr)