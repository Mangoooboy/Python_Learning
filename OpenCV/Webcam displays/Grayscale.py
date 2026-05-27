import cv2
cam =cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()