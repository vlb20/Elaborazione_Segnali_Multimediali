# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:04:16 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

''' FILTRO SPAZIALE ADATTATIVO

Filtraggio al variare della deviazione standard del rumore

'''

x = np.float64(io.imread("barbara.gif"))

M,N = x.shape

def filtra(x, sigma):
    sn2 = sigma**2 #varianza del rumore
    MED = ndi.uniform_filter(x, (7,7)) #media locale calcolata su blocchi 7x7
    VAR = ndi.uniform_filter(x**2, (7,7)) - (MED**2) #varianza locale
    #se var_locale > var rumore: restituisce un valore simile all'originale
        #altrimenti smoothing
    #y(i,j) - var_rumore/var_locale[y(i,j)- media_locale]
    y = x - (sn2/VAR)*(x-MED)
    return y

sigma = [5,10,15,20,25,30,35]
mse_noisy = np.zeros(len(sigma))
mse_adatt = np.zeros(len(sigma))
mse_media = np.zeros(len(sigma))
for i in range(len(sigma)):
    y = x + sigma[i]*np.random.randn(M,N) #immagine rumorosa
    xr_adatt = filtra(y, sigma[i])
    xr_media = ndi.uniform_filter(y, (7,7))
    mse_noisy[i] = np.mean((y-x)**2)
    mse_adatt[i] = np.mean((xr_adatt-x)**2)
    mse_media[i] = np.mean((xr_media-x)**2)
    
plt.figure()
plt.plot(sigma, mse_noisy, 'r-o')
plt.plot(sigma, mse_media, 'b-o')
plt.plot(sigma, mse_adatt, 'g-o')
plt.xlabel('sigma rumore')
plt.ylabel('MSE')
plt.legend(['rumorosa','filtro media','filtro adattativo'])
    