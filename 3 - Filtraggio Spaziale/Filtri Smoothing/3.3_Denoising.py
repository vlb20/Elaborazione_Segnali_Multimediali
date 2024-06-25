# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:49:02 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

''' DENOISING

1. Aggiungiamo rumore gaussiano bianco: noisy = x+n
       con n=d*np.random.randn(M,N) dove d è la dev. std. del rumore
       
2. Effettuo il denoising con i filtri a media mobile (al variare della finestra)

3. Misura quantitiva per stabilire quanto l'immagine elaborata sia simile all'originale
   -> MSE
'''

x = np.float64(io.imread("dorian.jpg"))

#Aggiungo il rumore
M,N = x.shape #ci servono le dimensioni per aggiungere il rumore
d = 20 #d basso non impatta molto
noise = d*np.random.randn(M,N) #rumore bianco gaussiano
img_noisy = x + noise #aggiungo il rumore -> immagine rumorosa

plt.figure()
plt.imshow(img_noisy, clim=None, cmap='gray')
plt.title("immagine rumorosa")

#filtro media aritmetica
list_k = [3,5,7,9]
mse = np.zeros(len(list_k))
psnr = np.zeros(len(list_k))
for index in range(len(list_k)):
    k = list_k[index] #dimensioni bloccjetto
    h = np.ones((k,k))/(k**2) #matrice k*k di "uni" e divido per k^2
    img_filt = ndi.correlate(img_noisy, h, mode='reflect')
    plt.figure()
    plt.imshow(img_filt, clim=None, cmap='gray')
    plt.title("immagine filtrata per k=%d" %k)
    mse[index] = np.mean((img_filt-x)**2)
    psnr[index] = 10*np.log10((255**2)/mse[index])

plt.figure()
plt.plot(list_k,mse,'r-*')
plt.xlabel('dimensione della finestra')
plt.ylabel('MSE')

plt.figure()
plt.plot(list_k,psnr,'r-*')
plt.xlabel('dimensione della finestra')
plt.ylabel('PSNR')

