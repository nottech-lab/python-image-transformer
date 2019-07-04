import cv2

def flip(originalImage, axes=[]):
    if len(axes) == 0:
        return None
    if len(axes) == 1:
        return flipOnce(originalImage,axes[0])
    else:
        return flip(flipOnce(originalImage,axes[0]), axes[1:])

def flipOnce(originalImage, axis='vertical'):
    if axis == 'vertical':
        return flipVertical(originalImage)
    if axis == 'horizontal':
        return flipHorizontal(originalImage)

def flipHorizontal(originalImage):
	return cv2.flip(originalImage, 1);

def flipVertical(originalImage):
	return cv2.flip(originalImage, 0);

import os
from os.path import isfile

#Example
#Load image from image/source/image1.jpg
originalImage = cv2.imread('images/source/image1.jpg')

#Flip the image, first vertical, then vertical and lastly horizontal
flipped = flip(originalImage, ['vertical', 'vertical', 'horizontal'])

cv2.imwrite('images/transformed/image1.jpg', flipped)
