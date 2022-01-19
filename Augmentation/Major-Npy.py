'''
This code creates a numpy array containing the the images belonging to the Major Category (X_Major.npy) and also creates 
Y_Major.npy file containing the corresponding classes of the X_Major file.

'''

import numpy as np
import os
import pandas as pd
from csv import writer
import cv2
from cv2 import imread
#df_skin = pd.read_csv(r'E:\RP 3 CALC\Big_Data.csv')
X = list()
Y = list()
D = list()
mel_ori = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\MEL')
#mel_aug = os.listdir(r'E:\RP 3 CALC\AUGMENTED\MEL')

bkl_ori = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\BKL')
bkl_aug = os.listdir(r'E:\RP 3 CALC\AUGMENTED\BKL')

bcc_ori = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\BCC')
bcc_aug = os.listdir(r'E:\RP 3 CALC\AUGMENTED\BCC')

nv_ori = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\NV')

ak_ori = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\AK')
ak_aug = os.listdir(r'E:\RP 3 CALC\AUGMENTED\AK')

df_ori = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\DF')
df_aug = os.listdir(r'E:\RP 3 CALC\AUGMENTED\DF')

scc_ori = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\SCC')
scc_aug = os.listdir(r'E:\RP 3 CALC\AUGMENTED\SCC')

vasc_ori = os.listdir(r'E:\RP 3 CALC\SL_CLASSES\VASC')
vasc_aug = os.listdir(r'E:\RP 3 CALC\AUGMENTED\VASC')


for i in range(len(mel_ori)):
    fname_image = mel_ori[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\MEL/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'mel'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
# for i in range(len(mel_aug)):
#     fname_image = mel_aug[i]
#     fname_ID = fname_image.replace('.jpg','')
#     file_to_read = r'E:\RP 3 CALC\Augment_Resize_76\MEL/' + str(fname_image)
#     img1 = imread(file_to_read)
#     #img1 = (img-np.mean(img))/np.std(img)
#     o1 = 'mel'
#     X.append(img1)
#     Y.append(o1)
#     print(i,' ',file_to_read,' ',o1)
    
for i in range(len(bkl_ori)):
    fname_image = bkl_ori[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\BKL/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'bkl'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(bkl_aug)):
    fname_image = bkl_aug[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\AUGMENTED\BKL/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'bkl'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(bcc_ori)):
    fname_image = bcc_ori[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\BCC/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'bcc'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(bcc_aug)):
    fname_image = bcc_aug[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\AUGMENTED\BCC/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'bcc'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(nv_ori)):
    fname_image = nv_ori[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\NV/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'nv'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
#OTHER CLASS CODE

for i in range(len(ak_ori)):
    fname_image = ak_ori[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\AK/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'others'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(ak_aug)):
    fname_image = ak_aug[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\AUGMENTED\AK/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'others'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(df_ori)):
    fname_image = df_ori[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\DF/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'others'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(df_aug)):
    fname_image = df_aug[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\AUGMENTED\DF/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'others'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(scc_ori)):
    fname_image = scc_ori[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\SCC/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'others'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(scc_aug)):
    fname_image = scc_aug[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\AUGMENTED\SCC/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'others'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(vasc_ori)):
    fname_image = vasc_ori[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\SL_CLASSES\VASC/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'others'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    
for i in range(len(vasc_aug)):
    fname_image = vasc_aug[i]
    fname_ID = fname_image.replace('.jpg','')
    file_to_read = r'E:\RP 3 CALC\AUGMENTED\VASC/' + str(fname_image)
    img1 = imread(file_to_read)
    #img1 = (img-np.mean(img))/np.std(img)
    o1 = 'others'
    X.append(img1)
    Y.append(o1)
    print(i,' ',file_to_read,' ',o1)
    

    
print(X)
print(Y)
c_mel = 0
c_bkl = 0
c_bcc = 0
c_nv = 0
c_other = 0

for i in Y:
    if i == 'mel':
        c_mel = c_mel + 1
    elif i == 'bkl':
        c_bkl = c_bkl + 1
    elif i == 'bcc':
        c_bcc = c_bcc + 1
    elif i == 'nv':
        c_nv = c_nv + 1
    elif i == 'other':
        c_other = c_other + 1

print("mel - ",c_mel)
print("bkl - ",c_bkl)
print("bcc - ",c_bcc)
print("nv - ",c_nv)
print("other - ", c_other)

X = np.array(X)
Y = np.array(Y)

print('The Shape of Y', Y.shape)
print('The Shape of X', X.shape)
np.save('E:/RP 3 CALC/X_major.npy',X)
np.save('E:/RP 3 CALC/Y_major.npy',Y)