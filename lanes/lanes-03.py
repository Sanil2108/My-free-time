import cv2
import numpy as np

image = cv2.imread("test_image.png")
lane_image = np.copy(image)

gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray, 50, 150)

cv2.imshow("result", canny_image)
cv2.waitKey(0)
