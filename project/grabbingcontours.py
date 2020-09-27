import numpy as np
import cv2

def grab_contours(cnts):
	if len(cnts) == 2:
		cnts = cnts[0]
	elif len(cnts) == 3:
		cnts = cnts[1]
	else:
		raise Exception(("Error Message"))

	return cnts
