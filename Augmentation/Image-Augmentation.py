

import numpy as np
import random
import os
import cv2
import pandas as pd
from csv import writer
import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt
from skimage import transform
from skimage.transform import rotate, AffineTransform
from skimage.util import random_noise
from skimage.filters import gaussian
from scipy import ndimage
from skimage.util import random_noise

def anti_rot(image):
    angle = random.randint(0,180)
    return rotate(image, angle)

def clock_rot(image):
    angle = random.randint(0,180)
    return rotate(image, -angle)

def hor_flip(image):
    return np.fliplr(image)

def ver_flip(image):
    return np.flipud(image)

transformations = {
    'rot_anti': anti_rot,
    'rot_clock': clock_rot,
    'hor_flip': hor_flip,
    'vert_flip': ver_flip,
    }

images_path = #location of initial unaugmented images#
augmented_path = #location of final augmented images#
images = []

for im in os.listdir(images_path):
    images.append(im)

images_to_generate = 4000

i = 1

while i<=images_to_generate:
    image_part = random.choice(images)
    image = os.path.join(images_path, image_part)
    original_image = imread(image)
    transformed_image = None
    print(i)
    n = 0
    transformation_count = random.randint(1, len(transformations))
    while n <= transformation_count:
        key = random.choice(list(transformations))
        print(i," - TRANSFORM - ",key)
        transformed_image = transformations[key](transformed_image)
        n = n + 1
    new_image_path = "%s/%s_%s_%s.jpg"%(augmented_path, image_part.replace('.jpg',''), key, i)
    plt.imsave(new_image_path, transformed_image)
    i = i + 1
    

print("DONE")