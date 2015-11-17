__author__ = 'rhys'

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Display the resulting frame if ret is true
	    cv2.imshow('frame', frame)



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()







