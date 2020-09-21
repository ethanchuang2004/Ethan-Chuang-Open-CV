from __future__ import print_function
from matplotlib import pyplot as plt
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
cv2.waitKey(0)

# chapter 4/6

# getting center of image for rotation
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

rotation = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, rotation, (w, h))
cv2.imshow("180 rotation", rotated)
cv2.waitKey(0)

# histograms for color chapter 7

chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	plt.plot(hist, color = color)
	plt.xlim([0, 256])

hist = cv2.calcHist([image], [0, 1, 2],
	None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))

plt.show()
