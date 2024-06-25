# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:34:12 2024

@author: vince
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import MyLibrary as ML
plt.close('all')

x = np.float64(io.imread("dorian.jpg"))

from skimage.util import random_noise
noisy = random_noise(x/255, 's&p') * 255
#La funzione random_noise richiede l'immagine nel range [0,1]

print("MSE della rumorosa", np.mean((x-noisy)**2))
plt.figure(1)
plt.subplot(121); plt.imshow(x, cmap='gray'); plt.title("Originale")
plt.subplot(122); plt.imshow(noisy, cmap='gray'); plt.title("Rumorosa")

list_k = [5,7,9]
mse = np.zeros(len(list_k))
for index in range(len(list_k)):
    k = list_k[index]
    y = ndi.median_filter(noisy, (k,k))
    plt.figure()
    plt.imshow(y, cmap='gray')
    plt.title('filtrata per k=%d' %k)
    mse[index] = np.mean((x-y)**2)

plt.figure()
plt.plot(list_k, mse, 'r-*')
plt.xlabel('dimensione della finestra')
plt.ylabel('MSE')