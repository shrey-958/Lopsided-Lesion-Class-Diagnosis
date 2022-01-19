''' 
This code creates a numpy array containing the the images belonging to the Minor Category (X_Minor.npy) and also creates 
Y_Minor.npy file containing the corresponding classes of the X_Minor file.

'''
import numpy as np
import os
import pandas as pd
from csv import writer
import cv2
from cv2 import imread
from skimage.io import imread, imsave
X = list()
Y = list()
D = list()
#ak_lista = os.listdir(r'E:\RP 3 CALC\LARGE WITHOUT HAIR')
ak_orig = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\AK')
ak_augm = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\Augmented\AK')

vasc_orig = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\VASC')
vasc_augm = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\Augmented\VASC')

scc_orig = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\SCC')
scc_augm = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\Augmented\SCC')

df_orig = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\DF')
df_augm = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\Augmented\DF')

for i in range(len(ak_orig)):
    fname_image = ak_orig[i]
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\AK/' + str(fname_image)
    img = imread(file_to_read)
    output = 'ak'
    X.append(img)
    print(i,' ',file_to_read)
    print(output)
    Y.append(output)
    
for i in range(len(ak_augm)):
    fname_image = ak_augm[i]
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\Augmented\AK/' + str(fname_image)
    img = imread(file_to_read)
    output = 'ak'
    X.append(img)
    print(i,' ',file_to_read)
    print(output)
    Y.append(output)
    
for i in range(len(vasc_orig)):
    fname_image = vasc_orig[i]
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\VASC/' + str(fname_image)
    img = imread(file_to_read)
    output = 'vasc'
    X.append(img)
    print(i,' ',file_to_read)
    print(output)
    Y.append(output)
    
for i in range(len(vasc_augm)):
    fname_image = vasc_augm[i]
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\Augmented\VASC/' + str(fname_image)
    img = imread(file_to_read)
    output = 'vasc'
    X.append(img)
    print(i,' ',file_to_read)
    print(output)
    Y.append(output)

for i in range(len(scc_orig)):
    fname_image = scc_orig[i]
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\SCC/' + str(fname_image)
    img = imread(file_to_read)
    output = 'scc'
    X.append(img)
    print(i,' ',file_to_read)
    print(output)
    Y.append(output)
    
for i in range(len(scc_augm)):
    fname_image = scc_augm[i]
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\Augmented\SCC/' + str(fname_image)
    img = imread(file_to_read)
    output = 'scc'
    X.append(img)
    print(i,' ',file_to_read)
    print(output)
    Y.append(output)
    
for i in range(len(df_orig)):
    fname_image = df_orig[i]
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\DF/' + str(fname_image)
    img = imread(file_to_read)
    output = 'df'
    X.append(img)
    print(i,' ',file_to_read)
    print(output)
    Y.append(output)
    
for i in range(len(df_augm)):
    fname_image = df_augm[i]
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\Augmented\DF/' + str(fname_image)
    img = imread(file_to_read)
    output = 'df'
    X.append(img)
    print(i,' ',file_to_read)
    print(output)
    Y.append(output)

print(Y)

X = np.array(X)
Y = np.array(Y)

print('The Shape of Y', Y.shape)
print('The Shape of X', X.shape)

np.save('E:/RP 3 CALC/X_minor.npy',X)
np.save('E:/RP 3 CALC/Y_minor.npy',Y)

