import cv2
import numpy as np

img = cv2.imread('dog_selfie.png',1)
print(img.shape[0:2])
height, width = img.shape[0:2]
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)# center là điểm xoay trung tâm, angle là góc tính theo độ , scale là thuộc tính tỉ lệ cho phù hợp với màn hình 
anh_xoay = cv2.warpAffine(img, rotationMatrix, (width, height))# Hàm được sử dụng 
cv2.imshow('dogcool', anh_xoay)
cv2.waitKey(0)



