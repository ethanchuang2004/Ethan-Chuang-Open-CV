import numpy as np
import cv2

# Chapter 6, rotation, image processing
def rotation(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w //2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotate = cv2.warpAffine(image, M, (w, h))

    return rotated
