import cv2
import numpy as np

image = cv2.imread('test_image.jpg')
copy_image = np.copy(image)
gray = cv2.cvtColor(copy_image, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg", gray)
