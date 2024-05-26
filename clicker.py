import cv2
import numpy as np
import pyautogui
import time
import datetime
import keyboard

upgrade_cycles = 0

# Load the image of the golden cookie
golden_cookie = cv2.imread('cookie.png', cv2.IMREAD_UNCHANGED)

if golden_cookie is None:
    print("Error: Golden cookie image not found. Please ensure 'cookie.png' is in the same directory as the script.")
    exit()

# Convert the golden cookie image to grayscale
golden_cookie_gray = cv2.cvtColor(golden_cookie, cv2.COLOR_BGR2GRAY)

def now():
    return datetime.datetime.now()


def find_golden_cookie():
    try:
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Convert the screenshot to grayscale
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Match the template (golden cookie) with the screenshot
        result = cv2.matchTemplate(screenshot_gray, golden_cookie_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Set a threshold to detect the golden cookie
        threshold = 0.45
        if max_val >= threshold:
            # Get the coordinates of the detected golden cookie
            x, y = max_loc
            h, w = golden_cookie_gray.shape
            center_x, center_y = x + w // 2, y + h // 2

            # Click the center of the golden cookie
            click(center_x, center_y)
            print(f'Golden cookie clicked at ({center_x}, {center_y}) at {now()}')
            return True
        return False
    except Exception as e:
        print(f"An error occurred {e} at {now()}")
        return False
    
def click_cookie():
    click(385,566)

def upgrade():
    global upgrade_cycles
    if(upgrade_cycles >= 600):
        click(2424,859)
        upgrade_cycles = 0
        print(f'attempted upgrade at {now()}')
    upgrade_cycles += 1

def display_coordinates():
    print(f"coordinates: ", get_position())

def click(x,y):
    if(y > 30 and y < 1380):
        pyautogui.click(x,y)

def get_position():
    return pyautogui.position()

def cycle():
    click_cookie()
    find_golden_cookie()
    #display_coordinates()
    #upgrade()


if __name__ == '__main__':
    print(f"Began program at {now()}")
    time.sleep(3)
    while True:
        try:
            if(keyboard.is_pressed('q')):
                print(f'Script stopped by user at {now()}')
                break
            cycle()
            time.sleep(0.1)
        except Exception as e:
            print(f"An unexpected error occurred {e} at {now()} ")
            break
