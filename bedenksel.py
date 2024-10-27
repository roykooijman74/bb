import cv2
import sys
import numpy as np
import signal
import win32gui
import pyautogui
from functools import partial
from PIL import ImageChops, ImageGrab
import time

# Enable all screen capturing for multiple monitors
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

# List of all windows (Smurfs) with coordinates and names
all_smurf_windows = [
    [2560, 0, 790, 460, 'Smurf 1'],
    [3414, 0, 790, 460, 'Smurf 2'],
    [4267, 0, 790, 460, 'Smurf 3'],
    [2560, 461, 790, 460, 'Smurf 4'],
    [3414, 461, 790, 460, 'Smurf 5'],
    [4267, 461, 790, 460, 'Smurf 6'],
    [2560, 921, 790, 460, 'Smurf 7'],
    [3414, 921, 790, 460, 'Smurf 8'],
    [4267, 921, 790, 460, 'Smurf 9'],
    [1770, 0, 790, 460, 'A Supersmurf'],
    [1770, 461, 790, 460, 'B MiniSmurf'],
    [1770, 921, 790, 460, 'C KickSmurf'],
]

def enable_ctrl_c():
    """Enable Ctrl-C interruption."""
    signal.signal(signal.SIGINT, signal.SIG_DFL)

class WindowsChecker:
    """Defines functions for checking windows and performing screen actions."""

    @staticmethod
    def check_active_windows(windows):
        """Return only the active windows."""
        active = []
        for window in windows:
            #print("Searching for: ", window[4])
            hwnd = win32gui.FindWindow(None, window[4])
            if hwnd:
                active.append(window)
        #print("Active windows: ", active)
        return active

    @staticmethod
    def check_color_at_x_y(x, y, r, g, b, variance=5):
        """Check if the pixel at (x, y) matches the specified color within a variance."""
        try:
            # Get the current pixel color
            pixel_color = pyautogui.pixel(x, y)
            #print(f"Checking color at ({x}, {y}): {pixel_color}")
            r_get, g_get, b_get = pixel_color
            # Check if each color is within the variance
            return (
                (r - variance <= r_get <= r + variance) and
                (g - variance <= g_get <= g + variance) and
                (b - variance <= b_get <= b + variance)
            )
        except Exception as e:
            print(f"Error checking color at ({x}, {y}): {e}")
            return False

def zoek_item_on_color(item, smurf):
    """Check if the specified item color matches on the smurf's screen."""
    x, y, r, g, b, _ = item[0], item[1], item[2], item[3], item[4], item[5]
    x1, y1, _, _, _ = smurf
    status = WindowsChecker.check_color_at_x_y(x + x1, y + y1, r, g, b, variance=20)
    if status:
        print(f"{smurf[4]}: {item[5]} found")
    # else:
    #     print(f"{smurf[4]}: {item[5]} NOT found")
    return status, smurf

def click_on_screen_for_smurf(smurf, x, y, offset_x=0, offset_y=0):
    x1, y1, _, _, _ = smurf
    absolute_x = x1 + x + offset_x
    absoluty_y = y1 + y + offset_y
    pyautogui.moveTo(absolute_x,absoluty_y)
    pyautogui.click(button='left')
    print("clicked on ", absolute_x, absoluty_y)
    #sys.exit()  # Exit the program

    time.sleep(0.2)


def pause_the_pause_button(active_smurf_windows):
    # ensure play/pause button is pauzed
    #move to pauze location to highligth the button
    pyautogui.moveTo(2560+566,14)
    item = [566, 14, 247, 250, 255, "pauze button"]   
    status, smurf = zoek_item_on_color(item, active_smurf_windows[0])
    if status:
        click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=0, offset_y=0)

def check_dr_t_talking(smurf):
    pass    
    
    # click_on_screen_for_smurf(smurf,23,145)
    # time.sleep(0.5)
    # item = [650, 261, 63, 53, 40, "dr t sunglass"]   
    # status, smurf = zoek_item_on_color(item, smurf)
    # if status:
    
    

def compare_images_with_confidence(first_image, current_image, confidence_threshold=0.8):
    # Convert images to grayscale for comparison
    first_gray = cv2.cvtColor(first_image, cv2.COLOR_BGR2GRAY)
    current_gray = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
    
    # Use template matching
    result = cv2.matchTemplate(current_gray, first_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    return max_val >= confidence_threshold

def detect_window_movement(window, confidence_threshold=0.8, interval=0.5, max_iterations=5):
    x, y, width, height, smurf_name = window
    # Capture the first image
    first_image = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    first_image = cv2.cvtColor(np.array(first_image), cv2.COLOR_RGB2BGR)  # Convert to OpenCV format
    iteration = 0
    stop_loop = False
    while stop_loop == False:
        time.sleep(interval)
        current_image = ImageGrab.grab(bbox=(x, y, x + width, y + height))
        current_image = cv2.cvtColor(np.array(current_image), cv2.COLOR_RGB2BGR)  # Convert to OpenCV format

        if compare_images_with_confidence(first_image, current_image, confidence_threshold):
            print(f"{smurf_name} Iteration {iteration + 1}: Image is stable (Confidence >= {confidence_threshold}).")
            stop_loop = True
        else:
            print(f"{smurf_name} Iteration {iteration + 1}: Image has changed (Confidence < {confidence_threshold}).")
            iteration += 1 
            if iteration == max_iterations:
                print(smurf_name, max_iterations, " checks done, stopped checking")
                stop_loop = True
        # Wait before the next check





def main():
    enable_ctrl_c()
    
    active_smurf_windows = WindowsChecker.check_active_windows(all_smurf_windows)

    pause_the_pause_button(active_smurf_windows)
    
    for smurf in active_smurf_windows:
        check_dr_t_talking(smurf)
    

    for y in range(80, 440, 30):
        for smurf in active_smurf_windows:
                pyautogui.moveTo(smurf[0]+180, y+smurf[1])
                time.sleep(0.2)
                pyautogui.click(button='left')

                # reward check code 
                item = [507, 350, 160, 220, 72, "reward"]
                status, smurf = zoek_item_on_color(item, smurf)
                if status:
                    click_on_screen_for_smurf(smurf,item[0],item[1])


                # item = [555, 203, 252, 190, 0, "zwarte garde midden"]   
                # status_midden, smurf = zoek_item_on_color(item, smurf)
                # if status_midden:
                #     print(smurf, status_midden)
                #     time.sleep(2.0)
                #     click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=480-555, offset_y=278-204)


                #     x1, y1 = smurf[:2]
                #     brown_coords = (x1 + 498, y1 + 206)
                #     for coords in [brown_coords]:
                #         pyautogui.moveTo(*coords)
                #         pyautogui.click(button='left')
                #         time.sleep(0.2)
                #     time.sleep(1.5)

                #     x1, y1 = smurf[:2]
                #     green_coords = (x1 + 433, y1 + 310)
                #     for coords in [green_coords]:
                #         pyautogui.moveTo(*coords)
                #         pyautogui.click(button='left')
                #         time.sleep(0.2)

                    # item = [485, 226, 200, 168, 80, "vernietigen bruin"]   
                    # status_bruin, smurf = zoek_item_on_color(item, smurf)
                    # if status_bruin:
                    #     input("Press Enter to...")  # Wait for user to press Enter
                    #     click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=0, offset_y=0)

                    #     item = [461, 300, 160, 216, 72, "vernietigen groen"]   
                    #     status_groen, smurf = zoek_item_on_color(item, smurf)
                    #     if status_groen:
                    #         click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=0, offset_y=0)
                    #         input("Press Enter to...")  # Wait for user to press Enter





                    # #detect_window_movement(smurf)
                    # item = [485, 226, 200, 168, 80, "vernietigen bruin"]   
                    # status_bruin, smurf = zoek_item_on_color(item, smurf)
                    # if status_bruin:
                    #     time.sleep(3.0)
                    #     click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=0, offset_y=0)
                    #     #detect_window_movement(smurf)
                    #     item = [461, 300, 160, 216, 72, "vernietigen groen"]   
                    #     status_groen, smurf = zoek_item_on_color(item, smurf)
                    #     if status_groen:
                    #         click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=0, offset_y=0)
                    #         sys.exit()


                # item = [427, 204, 211, 157, 6, "zwarte garde links"]
                # status, smurf = zoek_item_on_color(item, smurf)


if __name__ == "__main__":
    main()
