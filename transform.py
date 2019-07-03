#https://techtutorialsx.com/2019/04/21/python-opencv-flipping-an-image/
import cv2
originalImage = cv2.imread('images/source/image1.jpeg')
  
flipVertical = cv2.flip(originalImage, 0)
flipHorizontal = cv2.flip(originalImage, 1)
flipBoth = cv2.flip(originalImage, -1)

cv2.imwrite('images/transformed/image1.jpeg', flipVertical) 

#cv2.imshow('Original image', originalImage)
#cv2.imshow('Flipped vertical image', flipVertical)
#cv2.imshow('Flipped horizontal image', flipHorizontal)
#cv2.imshow('Flipped both image', flipBoth)
 
#cv2.waitKey(0)
#cv2.destroyAllWindows()