# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:05:35 2024

Visualizzazione di immagine

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

# x = io.imread("bianco_nero\dorian.jpg") #leggiamo il file
# (M,N) = x.shape #memorizziamo le dimensioni in M e N
# #shape estrae le informazioni sulla dimensione del file

# plt.figure(1)  #apre la figura 1 (vuota)
# plt.imshow(x, clim=[0,255], cmap='gray') #visualizziamo l'immagine
# #clim -> range livelli di grigio. Il sistema deve capire come assegnare i valori
# #a 0 il nero e a 255 il bianco
# #cmap -> visualizzazione in scala di grigio

# y = io.imread("bianco_nero\granelli.jpg")

# minimo = np.min(y)
# massimo = np.max(y)

# plt.figure(2)
# #plt.imshow(y, clim=[0,255], cmap='gray') 
# plt.imshow(y, clim=None, cmap='gray') 

# #LEGGIAMO LE IMMAGINI FORMATO RAW
# z=np.fromfile('bianco_nero\house.y', np.uint8)
# #gli diciamo su quanti bit leggerle

# #gli diciamo le dimensioni -> prende il vettore
# #e costruisce la matrice
# z = np.reshape(z, (512,512))
# plt.figure(3)
# plt.imshow(z, clim=[0,255], cmap='gray')


# #LETTURA IMMAGINI A COLORI
# k = io.imread("colore/fragole.jpg")

# R = k[:,:,0]
# #prendi tutte le righe e le colonne -> 0 canale di rosso
# plt.figure(4)
# plt.imshow(R, clim=[0,255], cmap='gray')
# plt.title('componente di rosso')
# #plt.colorbar()

# G = k[:,:,1]
# plt.figure(5)
# plt.imshow(G, clim=[0,255], cmap='gray')
# plt.title('componente di verde')

# B = k[:,:,2]
# plt.figure(6)
# plt.imshow(B, clim=[0,255], cmap='gray')
# plt.title('componente di blu')

#ANNULLIAMO LA COMPONENTE ROSSA
# M = k.shape[0] #numero di righe dell'immagine a colori
# N = k.shape[1] #numero di colonne di'immagine a colori
# R = np.zeros((M,N), z.dtype) #annullamento della componente di rosso
# #dtype -> fammela nel tipo dell'immagine
# s = np.stack((R,G,B), -1) #mettiamo insieme le componenti
# #lungo la dimensione del canale (-1)
# plt.figure()
# plt.imshow(s)
# plt.title('senza componente di rosso')

#ANNULLIAMO LA COMPONENTE VERDE
# M = k.shape[0] #numero di righe dell'immagine a colori
# N = k.shape[1] #numero di colonne di'immagine a colori
# G = np.zeros((M,N), z.dtype) #annullamento della componente di rosso
# #dtype -> fammela nel tipo dell'immagine
# s = np.stack((R,G,B), -1) #mettiamo insieme le componenti
# #lungo la dimensione del canale (-1)
# plt.figure()
# plt.imshow(s)
# plt.title('senza componente di verde')

# #ANNULLIAMO LA COMPONENTE VERDE
# M = k.shape[0] #numero di righe dell'immagine a colori
# N = k.shape[1] #numero di colonne di'immagine a colori
# B = np.zeros((M,N), z.dtype) #annullamento della componente di rosso
# #dtype -> fammela nel tipo dell'immagine
# s = np.stack((R,G,B), -1) #mettiamo insieme le componenti
# #lungo la dimensione del canale (-1)
# plt.figure()
# plt.imshow(s)
# plt.title('senza componente di blu')

R = io.imread('Washington_red.tif')
G = io.imread('Washington_green.tif')
B = io.imread('Washingyon_blue.tif')
I = io.imread('Washington_infrared.tif')
x = np.stack((R,G,B), 2)
plt.figure(1);
plt.imshow(x)
plt.show()
plt.title('RGB')
y = np.stack((I,G,B), 2)
plt.figure(1);
plt.imshow(y)
plt.show()
plt.title('IGB')

