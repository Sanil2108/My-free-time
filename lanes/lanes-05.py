import cv2
import numpy as np

image = cv2.imread("test_image.png")
lane_image = np.copy(image)

gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray, 120, 420)

mask = np.zeros_like(canny_image)
# image is a numpy array and the first parameter of shape should give the height of the image in pixels
height = image.shape[0]
# fillPoly function uses an array of polynomials.
polygons = np.array(np.array([
[(250, height), (600, 600), (1500, 600), (1500, height)]
]))
cv2.fillPoly(mask, polygons, 255)
masked_image = cv2.bitwise_and(canny_image, mask)

cv2.imshow("result", masked_image)

cv2.waitKey(0)