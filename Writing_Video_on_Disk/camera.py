import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    array, frame = cam.read()
    width = int(cam.get(3))
    height = int(cam.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height // 2, :width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height // 2:, :width // 2] = smaller_frame
    image[:height // 2, width // 2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height // 2:, width // 2:] = smaller_frame
    cv2.imshow("This is capturing video frames", image)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllwindwo()
