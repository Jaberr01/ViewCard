import cv2
import numpy as np

img = cv2.imread("image\Card.jpg")
#cv2.circle(img,(173,100), 10, (255,0,0),2) #I used these to find the corners of the card manually
#cv2.circle(img,(321,72), 10, (255,0,0),2)
#cv2.circle(img,(215,314), 10, (255,0,0),2)
#cv2.circle(img,(364,284), 10, (255,0,0),2)

width,height = 250,350 #typical width and height of card ratio-wise

InitialCoords = np.float32([[173,100],[321,72],[215,314],[364,284]]) #coords of corners of card

cv2.imshow("Cards",img) #show the original, unwarped image
i=0
speed = 2 #ammend to desired speed
for x in range(int(400/speed)): #turning view over the card
    i+=0.1*speed
    cv2.waitKey(2)
    FinalCoords = np.float32([[0+i,0+i],[width-i,0],[0+i,height-i],[width-i,height]])#new and straightened coords of corners of card

    matrixTrans = cv2.getPerspectiveTransform(InitialCoords, FinalCoords)  # Create a transformation matrix
    warped = cv2.warpPerspective(img, matrixTrans,(width, height))  # Apply transformation matrix on the card, and return an image object

    cv2.imshow("Card",warped) #show new frame of warped image

i = 40
for x in range(int(400/speed)): #turning back to straight view
    i-=0.1*speed
    cv2.waitKey(2)
    FinalCoords = np.float32([[0+i,0+i],[width-i,0],[0+i,height-i],[width-i,height]])

    matrixTrans = cv2.getPerspectiveTransform(InitialCoords, FinalCoords)  # Create a transformation matrix
    warped = cv2.warpPerspective(img, matrixTrans,(width, height))  # Apply transformation matrix on the card, and return an image object

    cv2.imshow("Card",warped)#show new frame of warped image

cv2.waitKey(0) #when code is over, press any key to terminate