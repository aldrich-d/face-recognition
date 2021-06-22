#In matrix there are three channel for color image(3d) rgb row x columns x 3(no. of channels) while one channel for black and white(2d)
# rows x columns
import cv2
img=cv2.imread("C:\\Users\\aldrich dsouza\\Downloads\\facebook post1.jpg",1) #1-indicates the rgb format, 0-indicates black and white
print(img.shape) #shape determines the rows x columns x channels
print(type(img)) #determines class of image which is numpy
print(img) #prints determine
resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("facebook post1",resized) #displays image where facbook post1 is the window name
cv2.waitKey(0) #0- unttil any key is pressed the image remains while for any positive value it displays in miliseconds
cv2.destroyAllWindows() #closes all window on single waitkey