import cv2
import numpy as np

# Initialize video capture object for webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to the grayscale frame
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find contours in the thresholded frame
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Create a blank mask image with the same shape as the frame
    mask = np.zeros_like(frame)

    # Loop over the contours and draw a red mask on the defect region
    count = 0  # initialize count variable
    for contour in contours:
        # Get the bounding box coordinates
        x, y, w, h = cv2.boundingRect(contour)

        # Create a mask on the defect region
        mask[y:y+h, x:x+w] = (0, 0, 255)

        count += 1  # increment count variable

    # Apply the mask to the frame
    masked_frame = cv2.bitwise_and(frame, mask)

    # Display the masked frame with defects highlighted
    cv2.putText(masked_frame, "Defects Detected: " + str(count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.imshow('Defects Detected', masked_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object and close windows
cap.release()
cv2.destroyAllWindows()
