import cv2
import numpy as np

image = cv2.imread("test_image.png")
lane_image = np.copy(image)

gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray, 120, 420)

mask = np.zeros_like(canny_image)
height = image.shape[0]
polygons = np.array(np.array([
    [(250, height), (600, 600), (1250, 600), (1500, height)]
]))
cv2.fillPoly(mask, polygons, 255)
masked_image = cv2.bitwise_and(canny_image, mask)


lines = cv2.HoughLinesP(masked_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
line_image = np.zeros_like(image)
for line in lines:
    x1, y1, x2, y2 = line.reshape(4)
    cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

combo_image = cv2.addWeighted(image, 0.8, line_image, 1, 1)

cv2.imshow("result", combo_image)
cv2.waitKey(0)