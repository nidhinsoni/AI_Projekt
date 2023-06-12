import cv2

# Initialize video capture object for webcam
cap = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blurred=cv2.GaussianBlur(gray, (7,7),0)

    # Apply adaptive thresholding to the grayscale frame
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find contours in the thresholded frame
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours and draw bounding boxes around the defects
    count = 0  # initialize count variable
    for contour in contours:
        # Get the bounding box coordinates
        x, y, w, h = cv2.boundingRect(contour)

        # Draw a red rectangle around the defect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)

        count += 1  # increment count variable

    # Display the original frame with contours drawn
    cv2.putText(frame, "Defects Detected: " + str(count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.imshow('Defects Detected', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object and close windows
cap.release()
cv2.destroyAllWindows()
