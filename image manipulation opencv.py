import cv2
import numpy as np

image = cv2.imread('image.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(image, (300, 300))

(h, w) = image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

edges = cv2.Canny(image, 100, 200)

cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Edge Detection', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
