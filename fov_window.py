import cv2
import numpy as np
import threading

LOWER_COLOR = np.array([140, 111, 160])
UPPER_COLOR = np.array([148, 154, 194])


def show_detection_window(grabber, window_toggled):
    while window_toggled():
        screen = grabber.get_screen()
        hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, LOWER_COLOR, UPPER_COLOR)
        highlighted = cv2.bitwise_and(screen, screen, mask=mask)
        blurred = cv2.GaussianBlur(highlighted, (0, 0), sigmaX=1, sigmaY=1)
        dimmed = cv2.addWeighted(screen, 0.1, np.zeros(screen.shape, dtype=screen.dtype), 0, 0)
        result = cv2.add(blurred, dimmed)

        if screen.shape[0] < 500 or screen.shape[1] < 500:
            result_resized = cv2.resize(result, (500, 500))
        else:
            result_resized = result

        cv2.imshow('DETECTION WINDOW FOR FTNAIMZ', result_resized)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


def toggle_window(ftnaim):
    ftnaim.window_toggled = not ftnaim.window_toggled

    if ftnaim.window_toggled:
        threading.Thread(target=show_detection_window, args=(ftnaim.grabber, lambda: ftnaim.window_toggled),
                         daemon=True).start()