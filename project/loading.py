from __future__ import print_function
from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np
import grabbingcontours
import glob

# https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
# some code i found from online to help with auto canny detection for
# thresholds

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged

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

# code to help find dominant color of image found at
# https://www.timpoulsen.com/2018/finding-the-dominant-colors-of-an-image.html
img = image
height, width, _ = np.shape(img)

# calculate the average color of each row of our image
avg_color_per_row = np.average(img, axis=0)

# calculate the averages of our rows
avg_colors = np.average(avg_color_per_row, axis=0)

# avg_color is a tuple in BGR order of the average colors
# but as float values
print(f'avg_colors: {avg_colors}')

# so, convert that array to integers
int_averages = np.array(avg_colors, dtype=np.uint8)
print(f'int_averages: {int_averages}')

# create a new image of the same height/width as the original
average_image = np.zeros((height, width, 3), np.uint8)
# and fill its pixels with our average color
average_image[:] = int_averages

# finally, show it side-by-side with the original
cv2.imshow("Avg Color", average_image)


# Chapter 9 Threshholding / Chapter 8 Blurring

cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("black and white, blurred", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

blurImage = cv2.Canny(blurred, 30, 150)

cv2.waitKey(0)
cv2.destroyAllWindows()

(contour, _) = cv2.findContours(blurImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Using Canny Detection, I count {} shapes in this image".format(len(contour)))

circles = blurImage.copy()
cv2.drawContours(circles, contour, -1, (255, 255, 255), 2)
cv2.imshow("blur edge detection", circles)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Chapter 10 Edge Detection

(T, thresh) = cv2.threshold(image, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("thresholding", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

threshImage = auto_canny(thresh)

(contour2, _) = cv2.findContours(threshImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Using Thresholding, I count {} shapes in this image".format(len(contour2)))

circles2 = threshImage.copy()
cv2.drawContours(circles2, contour2, -1, (255, 0, 255), 2)
cv2.imshow("threshholding edge detection", circles2)

cv2.waitKey(0)
cv2.destroyAllWindows()
