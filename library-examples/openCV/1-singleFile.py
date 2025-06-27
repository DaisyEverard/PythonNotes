# OpenCV is an open source face detection library
# The haarcascade is a config files

import cv2

detect = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
imp_img = cv2.VideoCapture("./images/henryCavill1.jpg")
# imported image

res, img = imp_img.read()
# res is True/False if read worked is not
# img is the pixel dimensions of the image

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# The haarcascade used was trained for greyscale images so we need to convert ours to grey

faces = detect.detectMultiScale(grey, 1.3, 5)
# input image, scale factor, minimum neighbour
# "draws square" over face and returns coordinates
#  see example in example-coords.png

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
    # rectangle (image, pt1, pt2, color, thickness)
    # pt1 and pt2 are opposite corners of the rectangle

cv2.imshow("Cavill Image", img)
cv2.waitKey(0)
# display the image with a given title
# waitKey is how long the image will stay open for
# setting to zero means until I close it

imp_img.release()
# closes file or capturing device if video. Deallocates memory
cv2.destroyAllWindows()

