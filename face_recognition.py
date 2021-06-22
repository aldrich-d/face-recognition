import cv2
img=cv2.imread("C:\\Users\\aldrich dsouza\\Downloads\\facebook post1.jpg",1) #1-indicates the rgb format, 0-indicates black and white
#face detection ->image ->cascade classifier -> opencv -> numpy array-> display rectangular box
face_cascade=cv2.CascadeClassifier("C:\\Users\\aldrich dsouza\\Downloads\\Face Detect\\haarcascade_frontalface_default.xml") #creating a cascade classifier object
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #reading the image
faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.8, minNeighbors=5) #reading image as gray scale, searching the coordinates
for x,y,w,h in faces:
    img= cv2.rectangle(img,(x,y),(x+w,y+h),(122,0,500),3) #(x,y) are coordintes with w and h as the width and height , color is given in (R(122),G(0),B(500)) format where 3 is thickness of the rectangle
resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #optional
cv2.imshow("my image",resized)
cv2.waitKey(0)