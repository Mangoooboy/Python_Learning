import cv2
import os
cam = cv2.VideoCapture(0)
if not os.path.exists("../Images"):
    os.mkdir("../Images")
cam = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == 32:
        filename = f"../Images/image_{count}.jpg"

        cv2.imwrite(filename, frame)

        print("Saved:", filename)
        count = count + 1

    elif key == 27:
        break
cam.release()
cv2.destroyAllWindows()