import cv2
import numpy as np

image = cv2.imread('image.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
median_blur = cv2.medianBlur(image, 5)
bilateral_filter = cv2.bilateralFilter(image, 9, 75, 75)

edges_canny = cv2.Canny(image, 100, 200)
edges_sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
edges_sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
edges_laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)

cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Gaussian Blurred', blurred_image)
cv2.imshow('Median Blurred', median_blur)
cv2.imshow('Bilateral Filtered', bilateral_filter)
cv2.imshow('Canny Edge Detection', edges_canny)
cv2.imshow('Sobel X Edge Detection', edges_sobel_x)
cv2.imshow('Sobel Y Edge Detection', edges_sobel_y)
cv2.imshow('Laplacian Edge Detection', edges_laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
