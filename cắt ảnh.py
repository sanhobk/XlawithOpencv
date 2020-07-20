import cv2
img = cv2.imread('dog_selfie.png')
height, width = img.shape[0:2]#trích xuất chiều cao và chiều rộng của ảnh
startRow = int(height*.15)#Hàng bắt đầu từ hàng số 15
startCol = int(width*.15)#Cột bắt đầu từ cột số 15
endRow = int(height*.85)#Hàng kết thúc từ hàng số 85
endCol = int(width*.85)#Cột kết thúc từ cột số 85
croppedImg= img[startRow:endRow, startCol:endCol]#Ánh xạ các giá trị trên vào hình ảnh gốc
cv2.imshow('Original Image', img)#show ảnh thường
cv2.imshow('Cropped Image', croppedImg)#show ảnh đã crop
cv2.waitKey(0)