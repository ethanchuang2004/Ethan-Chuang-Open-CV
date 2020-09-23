Ethan Chuang
Advanced Honors Computer Science
Beginning OpenCV Project

Chapter 3, 4, 6, 7, 8, 9 are represented in my code.

Chapter 3 - arg parser function

just used the arg parse function to accept the user's path to the file and load the image

Chapter 4 - pixel manipulation/arithmetic, rotation function

used pixel arithmetic to find the center of the image for the basis of rotation

used rotation function to rotate the image 180 degrees

Chapter 7 - histogram creation

used histogram functions to create a 2d color histogram of the three primary colors r,g,b

Chapter 8, 9 - Blurring and Thresholding

used blurring and then thresholding to set up edge detection, but I am not sure on the optimal combination of blurring and thresholding to help with
edge detection

Chapter 10, 11 - edge detection and contours

used edge detection and contours to count the amount of "stars" in Starry Night painting


Instructions:

Make sure all packages from the openCV textbook are installed.

After moving into the project folder, run this command: python loading.py --image /Users/egc/Documents/GitHub/Ethan-Chuang-Open-CV/project/starrynight.webp

Then a default image, unedited will load, where you can press spacebar.

After you press spacebar, a 180 flipped upside down image will appear.

Then, if you press space once again, the 2d histogram will appear showing the variance of colors.

You will then have to press the x in the corner of the histogram graph, where a black and white image will show up, unflipped.

This image will be modified with blurs and thresholding in the next buttons of space pressing, and will close to show the terminal window showing the amount of stars.
