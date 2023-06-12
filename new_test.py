import cv2
import numpy as np

# Initialize video capture object for webcam
cap = cv2.VideoCapture(1)

kernel=np.ones((5,5),np.uint8)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blurred=cv2.GaussianBlur(gray, (5,5), 0)
    (T, thresh) = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY)

    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Display the original frame with contours drawn
    cv2.imshow('Defects Detected', opening)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object and close windows
cap.release()
cv2.destroyAllWindows()
