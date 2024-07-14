import cv2
import numpy as np
import pyautogui
import time
import datetime
import keyboard
import pytesseract

cycles = 0
last_upgrade = 0

# Load the image of the golden cookie
golden_cookie = cv2.imread('cookie.png', cv2.IMREAD_UNCHANGED)

if golden_cookie is None:
    print("Error: Golden cookie image not found. Please ensure 'cookie.png' is in the same directory as the script.")
    exit()

# Convert the golden cookie image to grayscale
golden_cookie_gray = cv2.cvtColor(golden_cookie, cv2.COLOR_BGR2GRAY)

# Set up Tesseract executable path for Windows (adjust the path if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def now():
    return datetime.datetime.now()


def click_cookie():
    click(385, 566)
    # print(f'Cookie clicked at {now()}')


def find_golden_cookie():
    try:
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Convert the screenshot to grayscale
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Match the template (golden cookie) with the screenshot
        result = cv2.matchTemplate(
            screenshot_gray, golden_cookie_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Set a threshold to detect the golden cookie
        threshold = 0.41
        if max_val >= threshold:
            # Get the coordinates of the detected golden cookie
            x, y = max_loc
            h, w = golden_cookie_gray.shape
            center_x, center_y = x + w // 2, y + h // 2

            # Click the center of the golden cookie if it is not near upgrades
            if (center_x < 2200):
                click(center_x, center_y)
            # print(f'Golden cookie clicked at ({center_x}, {center_y}) at {now()}')
            return
        # print(f'Golden cookie not found at {now()}')
        return
    except Exception as e:
        print(f"An error occurred {e} at {now()}")
        return False


def display_coordinates():
    if (keyboard.is_pressed('w')):
        print(f"coordinates: {get_position()} at {now()}")
        pass


def upgrade():
    click(2420, 220)
    # click(2420,860)
    # print(f'attempted upgrade at {now()}')


def get_cookie_count():
    try:
        # Define the region of interest (ROI) for the cookie count
        # You may need to adjust these coordinates based on your screen resolution and game window position
        # Example coordinates, adjust accordingly
        x, y, width, height = 260, 160, 240, 60

        # Take a screenshot of the defined region
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Convert the screenshot to grayscale
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Use Tesseract to do OCR on the image
        cookie_count_text = pytesseract.image_to_string(screenshot_gray)

        # Clean up the OCR result to extract the number
        cookie_count = ''.join(filter(str.isdigit, cookie_count_text))

        if cookie_count:
            cookie_count = int(cookie_count)

        try:
            if cookie_count is not None:
                # print(f'Current cookie count: {cookie_count} at {now()}')
                pass
            else:
                print(f'Could not read cookie count at {now()}')
        except Exception as e:
            print(f"An unexpected error occurred: {e} at {now()}")
            return

    except Exception as e:
        print(
            f"An error occurred while reading the cookie count: {e} at {now()}")
        return None


def click(x, y):
    if (y > 30 and y < 1380):
        pyautogui.click(x, y)


def get_position():
    return pyautogui.position()


def cycle():
    # start_time = now()
    click_cookie()
    find_golden_cookie()
    # display_coordinates()
    # get_cookie_count()
    # print(f'this cycle took {now() - start_time} to complete')
    # global cycles
    # global last_upgrade
    # cycles += 1
    # if(cycles >= 100):
    #     upgrade()
    #     cycles = 0
    #     if(last_upgrade == 0):
    #         last_upgrade = now()
    #     else:
    #         print(f'Upgrade done in this time: {now() - last_upgrade}')
    #         last_upgrade = now()

    return


if __name__ == '__main__':
    print(f"Began program at {now()}")
    time.sleep(3)
    while True:
        try:
            if (keyboard.is_pressed('q')):
                print(f'Script stopped by user at {now()}')
                break
            cycle()
            # time.sleep(0.1)
        except Exception as e:
            print(f"An unexpected error occurred {e} at {now()} ")
            break
