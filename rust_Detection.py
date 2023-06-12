import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image")
args = vars(ap.parse_args())

# define the list of boundaries
boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128])
]

# Create a VideoCapture object to read from the camera (0 represents the default camera)
cap = cv2.VideoCapture(0)

# Set the window properties
cv2.namedWindow("images", cv2.WINDOW_NORMAL)
cv2.resizeWindow("images", 1980, 1080)  # Set the desired window size

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply the mask
        mask = cv2.inRange(frame, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask=mask)
        # show the images
        cv2.imshow("images", np.hstack([frame, output]))

    if cv2.waitKey(1) == ord('q'):  # Exit when 'q' is pressed
        break

# Release the VideoCapture object and close windows
cap.release()
cv2.destroyAllWindows()
