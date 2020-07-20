import cv2
img = cv2.imread('dog_selfie.png',1)
blur_img = cv2.GaussianBlur(img, (99,99), 0)
cv2.imshow('Original', img)
cv2.imshow('BlurImg', blur_img)
cv2.waitKey(0)