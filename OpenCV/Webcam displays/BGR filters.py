import cv2

camera = cv2.VideoCapture(0)
while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)

    blue = frame.copy()
    green = frame.copy()
    red = frame.copy()

    blue[:,:,1] = 0
    blue[:,:,2] = 0

    green[:,:,0] = 0
    green[:,:,2] = 0

    red[:,:,0] = 0
    red[:,:,1] = 0

    cv2.imshow("blue",blue)
    cv2.imshow("green",green)
    cv2.imshow("red",red)
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
    
    if key == 27:
        break
camera.release()
cv2.destroyAllWindows()