from __future__ import print_function
from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np
import grabbingcontours


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
cv2.destroyAllWindows()

# histograms for color chapter 7
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	plt.plot(hist, color = color)
	plt.xlim([0, 256])


hist = cv2.calcHist([image], [0, 1, 2],
	None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

cv2.destroyAllWindows()
plt.show()


# Chapter 9 Threshholding / Chapter 8 Blurring

cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("black and white, blurred", blurred)

canny = cv2.Canny(blurred, 30, 150)
cv2.imshow("blur canny", canny)

cnts = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Using Gaussian Blurring, I count {} circles in this image".format(len(cnts)))
#cnts = grabbingcontours.grab_contours(cnts)

cannyI = canny.copy()
cv2.drawContours(cannyI, cnts, -1, (0, 255, 0), 2)
cv2.imshow("blur edge detection", cannyI)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Chapter 10 Edge Detection

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("thresholding", thresh)

canny2 = cv2.Canny(thresh, 30, 150)
cv2.imshow("thresh canny", canny2)

cnts2 = cv2.findContours(canny2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Using Thresholding and Gaussian Blurring, I count {} circles in this image".format(len(cnts)))
#cnts2 = grabbingcontours.grab_contours(cnts)

"""
cannyI2 = canny.copy()
cv2.drawContours(cannyI2, cnts2, -1, (0, 255, 0), 2)
cv2.imshow("threshholding edge detection", cannyI2)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
