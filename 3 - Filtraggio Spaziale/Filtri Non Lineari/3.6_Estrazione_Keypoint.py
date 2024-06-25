# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:11:37 2024

@author: vince
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi


plt.close('all')

x = np.float64(io.imread('tetto.png'))

#Creazione dei filtri per il calcolo delle derivate
V = np.array([[0,-1,0],[0,1,0],[0,0,0]], dtype=np.float64)
H = np.array([[0,0,0],[-1,1,0],[0,0,0]], dtype=np.float64)
D1 = np.array([[-1,0,0],[0,1,0],[0,0,0]], dtype=np.float64)
D2 = np.array([[0,0,-1],[0,1,0],[0,0,0]], dtype=np.float64)

#Calcolo delle derivate nelle varie direzioni
v = ndi.correlate(x,V)
h = ndi.correlate(x,H)
d1 = ndi.correlate(x,D1)
d2 = ndi.correlate(x,D2)

#Quadrati delle derivate
vv = v**2
hh = h**2
dd1 = d1**2
dd2 = d2**2

# Calcolo su finestra scorrevole delle medie dei valori al quadrato 
Qv  = ndi.uniform_filter(vv , (3,3))
Qh  = ndi.uniform_filter(hh , (3,3))
Qd1 = ndi.uniform_filter(dd1, (3,3))
Qd2 = ndi.uniform_filter(dd2, (3,3))

#Calcolo del minimo
Qmin = np.minimum(np.minimum(Qv,Qh), np.minimum(Qd1,Qd2))

#Calcolo dei punti salienti -> valore massimo di Qmin
MQmin = ndi.generic_filter(Qmin, np.max, (3,3))
SP = (Qmin > 20) & (Qmin == MQmin) #mappa binaria

# Visualizzazione
plt.figure(); 
plt.subplot(1,2,1);
plt.imshow(x , clim=[0,255],cmap='gray'); plt.title('Immagine test');
plt.subplot(1,2,2);
plt.imshow(SP, clim=[0,1],cmap='gray'); plt.title('Mappa dei Keypoint');