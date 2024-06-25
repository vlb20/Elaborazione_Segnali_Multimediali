# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:54:22 2024

@author: vince
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

x = np.float32(io.imread("granelli.jpg"))
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')

#Full-Scale Histogram Stretch
mini = np.min(x)
maxi = np.max(x)
K = 256
y = ((K-1)*(x-mini))/(maxi-mini)

plt.figure(2)
plt.imshow(y, clim=[0,255], cmap='gray')