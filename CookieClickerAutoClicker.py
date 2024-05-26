import cv2
import numpy as np
import pyautogui
import time
import datetime


def now():
    return datetime.datetime.now()

def find_golden_cookie(golden_cookie):
    #Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    #Match the golden cookie image with the screenshot
    result = cv2.matchTemplate(screenshot, golden_cookie, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #Set a threshold to detect the cookie
    threshold = 0.5
    if max_val >= threshold:
        #Get the coordinates of the detected golden cookie
        x, y = max_loc
        h, w = golden_cookie.shape
        center_x, center_y = x + w // 2, y + h // 2

        #Click on the center of the golden cookie
        pyautogui.click(center_x, center_y)

        print(f'Golden cookie clicked at ({center_x,} {center_y}) at {now()}')
        return True
    return False

if __name__ == '__main__':
    print(f'Program began at {now()}')
    golden_cookie = cv2.imread('golden_cookie.png', cv2.IMREAD_UNCHANGED)

    while True:
        try:
            if find_golden_cookie(golden_cookie):
                time.sleep(1)
            else:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print(f'Script stopped at {now()}')
            break


