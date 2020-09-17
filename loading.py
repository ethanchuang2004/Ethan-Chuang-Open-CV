from __future__ import print_function
import argparse
import cv2
import numpy as np

# getting path to image, Chapter 3
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("image", image)
cv2.watKey(0)


# Chapter 6, rotation, image processing
def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w //2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotate = cv2.warpAffine(image, M, (w, h))

    return rotated
