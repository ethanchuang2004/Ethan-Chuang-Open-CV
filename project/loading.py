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

cv2.waitKey(0)
cv2.destroyAllWindows()

blurImage = cv2.Canny(blurred, 30, 150)

cv2.waitKey(0)
cv2.destroyAllWindows()

(contour, _) = cv2.findContours(blurImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Using Gaussian Blurring, I count {} circles in this image".format(len(contour)))

circles = blurImage.copy()
cv2.drawContours(circles, contour, -1, (0, 255, 0), 2)
cv2.imshow("blur edge detection", circles)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Chapter 10 Edge Detection

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("thresholding", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

threshImage = cv2.Canny(thresh, 10, 30)

(contour2, _) = cv2.findContours(threshImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Using Thresholding and Gaussian Blurring, I count {} circles in this image".format(len(contour2)))

circles2 = threshImage.copy()
cv2.drawContours(circles2, contour2, -1, (0, 255, 0), 2)
cv2.imshow("threshholding edge detection", circles2)

cv2.waitKey(0)
cv2.destroyAllWindows()
