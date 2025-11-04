#Real-Time Color Detection using HSV Trackbars in OpenCV
import cv2
import numpy as np

def nothing(x):
    pass  # placeholder for trackbar callback

def create_trackbars():
    """Create HSV trackbars for color tuning."""
    cv2.namedWindow("Trackbars")
    cv2.createTrackbar("LH", "Trackbars", 0, 179, nothing)
    cv2.createTrackbar("LS", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("LV", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("UH", "Trackbars", 179, 179, nothing)
    cv2.createTrackbar("US", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("UV", "Trackbars", 255, 255, nothing)

def get_hsv_range():
    """Read current positions of trackbars."""
    lh = cv2.getTrackbarPos("LH", "Trackbars")
    ls = cv2.getTrackbarPos("LS", "Trackbars")
    lv = cv2.getTrackbarPos("LV", "Trackbars")
    uh = cv2.getTrackbarPos("UH", "Trackbars")
    us = cv2.getTrackbarPos("US", "Trackbars")
    uv = cv2.getTrackbarPos("UV", "Trackbars")
    lower = np.array([lh, ls, lv])
    upper = np.array([uh, us, uv])
    return lower, upper

def main():
    cap = cv2.VideoCapture(0)
    create_trackbars()

    print("🎨 Adjust the HSV sliders to isolate a specific color. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get HSV range from trackbars
        lower, upper = get_hsv_range()

        # Create a binary mask for the color
        mask = cv2.inRange(hsv, lower, upper)

        # Bitwise-AND mask and original image
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Show all three windows
        cv2.imshow("Original", frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("Color Detection", result)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
