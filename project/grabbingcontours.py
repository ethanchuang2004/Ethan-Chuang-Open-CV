import numpy as np
import cv2

def grab_contours(cnts):
	if len(cnts) == 2:
		cnts = cnts[0]
	elif len(cnts) == 3:
		cnts = cnts[1]
	else:
		raise Exception(("Contours tuple must have length 2 or 3, "
			"otherwise OpenCV changed their cv2.findContours return "
			"signature yet again. Refer to OpenCV's documentation "
			"in that case"))

	return cnts
