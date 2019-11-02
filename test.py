import sys
import os
from os.path import isabs, isfile, isdir, join, dirname, basename, exists, splitext, relpath
from os import remove, getcwd, makedirs, listdir, rename, rmdir, system
from shutil import move
import glob
import regex as re
import numpy as np
import numpy
import pickle
import random
import itertools
import time
import subprocess
from subprocess import call
import json
from pathlib import Path
import cv2 as cv
import cv2
import dlib


# 
# open image
# 
img = cv.imread( "face1.jpg" )


def show_image(img):
    name = "image"
    cv2.imshow(name, img)
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.destroyWindow(name)

#show_image(img)


# 
# load up the face detector
# 
detector  = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")
# Ask the detector to find the bounding boxes of each face. The 1 in the
# second argument indicates that we should upsample the image 1 time. This
# will make everything bigger and allow us to detect more faces.
dets = detector(img, 1)
# initialize by the number of faces
faces = [None]*len(dets)

# 
# Start up the face finder
# 
for index, d in enumerate(dets):
    shape = predictor(img, d)
    faces[index] = shape

# 
# store the first face as an array
#
if len(faces) == 0:
    print("no faces found")
else:
    face_points_as_array = np.empty(( len(faces), 2), dtype=np.int32)
    face_1_shape = faces[0]
    for each_part_index in range(face_1_shape.num_parts):
        point = shape.part(each_part_index)
        
        face_points_as_array[each_part_index][0] = point.x
        face_points_as_array[each_part_index][1] = point.y



# def ndarray_to_list(ndarray):
#     if type(ndarray) != numpy.ndarray:
#         return ndarray
#     else:
#         as_list = ndarray.tolist()
#         new_list = []
#         for each in as_list:
#             new_list.append(ndarray_to_list(each))
#         return new_list



# def with_points(img, array_of_points, color=(255, 255, 00), radius=3):
#     img_copy = img.copy()
#     for x, y in array_of_points:
#         cv.circle(img_copy, (x, y), radius, color, thickness=-1, lineType=8, shift=0)
#     return img_copy