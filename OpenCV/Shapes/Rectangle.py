import cv2
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame,
                  (100, 100),
                  (400, 300),
                  (0,0, 0),
                  1)
    cv2.imshow('Rectangle',frame)

    if cv2.waitKey(1) ==27:
        break
cam.release()
cv2.destroyAllWindows()

