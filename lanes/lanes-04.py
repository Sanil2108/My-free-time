import cv2
import numpy as np

import matplotlib.pyplot as plt

image = cv2.imread("test_image.png")
lane_image = np.copy(image)

gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray, 50, 150)

mask = np.zeros_like(image)


plt.imshow(image)
plt.show()

# cv2.imshow("result", canny_image)
# cv2.waitKey(0)