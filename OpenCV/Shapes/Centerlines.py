import cv2

cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()

    frame = cv2.flip(frame, 1)

    h, w, c = frame.shape

    cv2.line(frame,
             (w//2, 0),
             (w//2, h),
             (0,5,0),
             1)

    cv2.line(frame,
             (0, h//2),
             (w, h//2),
             (0,5,0),
             1)

    cv2.imshow("Center Lines", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()

cv2.destroyAllWindows()