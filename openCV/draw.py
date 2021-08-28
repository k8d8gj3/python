import cv2 as cv
import numpy as np

# (500,500,3) = height, width, num of color channels
blank = np.zeros((500,500,3), dtype="uint8")

# 1. Paint the image a certain color
# blank[200:300, 300:400] = 0,0,255
# print(blank)
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)

# 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)

# 4. Draw a line
# cv.line(blank, (100,250), (300, 400), (255,255,255), thickness=3)

# 5. Write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Circle', blank)

cv.waitKey(0)