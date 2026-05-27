import cv2
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)

    cv2.putText(frame,
                "OpenCV",
                (10,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,0),2)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1)==27:
        break

cam.release()
cv2.destroyAllWindows()