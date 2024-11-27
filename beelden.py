''' my python code for automating boring stuff in boom beach'''
import sys
from functools import partial
import win32gui
import pyautogui
from PIL import ImageGrab
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import time
import win32api
import win32con
import threading
import os

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

# Define the control key
CTRL_KEY = win32con.VK_CONTROL

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
    [1770, 921, 790, 460, 'C KickSmurf'],
]
#    [1770, 0, 790, 460, 'A Supersmurf'],
#    [1770, 461, 790, 460, 'B MiniSmurf'],



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

def zoek_item_on_color(item, smurf):
    """Check if the specified item color matches on the smurf's screen."""
    x, y, r, g, b, _ = item[0], item[1], item[2], item[3], item[4], item[5]
    x1, y1, _, _, _ = smurf
    status = WindowsChecker.check_color_at_x_y(x + x1, y + y1, r, g, b, variance=20)
#    if status:
#        print(f"{smurf[4]}: {item[5]} found")
    # else:
    #     print(f"{smurf[4]}: {item[5]} NOT found")
    return status, smurf

def click_on_screen_for_smurf(smurf, x, y, offset_x=0, offset_y=0):
    '''Clicking on the absolute mouse position for a smurf based on x,y provided.'''
    x1, y1, _, _, _ = smurf
    absolute_x = x1 + x + offset_x
    absoluty_y = y1 + y + offset_y
    pyautogui.moveTo(absolute_x,absoluty_y)
    pyautogui.click(button='left')
    #print("clicked on ", absolute_x, absoluty_y)
    #sys.exit()  # Exit the program

    time.sleep(0.1)

def search_image(image_path, npcteller, offset=0, confidencevalue=0.7, rois=None, wait=0.1):
    '''Search for an image within specified regions of interest (ROIs)'''
    rois = rois or []
    status, found_x, found_y = 0, None, None

    for roi in rois:
        x1, y1, width, length, name = roi
        location = pyautogui.locateCenterOnScreen(image_path,
                                                confidence=confidencevalue,
                                                region=(x1, y1, width, length)
                                                )

        if location:
            x, y = location[0], location[1] + offset
            pyautogui.moveTo(x, y)
            time.sleep(wait)
            pyautogui.click(button='left')
            status += 1
            print(npcteller, name, "destroyed at", x, y)
            npcteller += 1
            found_x, found_y = x, y

    return npcteller, status, found_x, found_y



def pause_the_play_button(active_smurf_windows):
    '''The play button will be pauzed'''
    pyautogui.moveTo(2560+566,14)
    item = [566, 14, 247, 250, 255, "pauze button"]
    status, smurf = zoek_item_on_color(item, active_smurf_windows[0])
    if status:
        click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=0, offset_y=0)
        #print("pauze pressed")
    #else:
        #print("no need to press pauze")

def start_the_play_button(active_smurf_windows):
    '''The play button will be started'''
    # ensure play/pause button is pauzed
    #move to pauze location to highligth the button
    pyautogui.moveTo(2560+566,14)
    item = [562, 17, 247, 250, 255, "start button"]
    status, smurf = zoek_item_on_color(item, active_smurf_windows[0])
    if status:
        click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=0, offset_y=0)
        #        print("play pressed")
    #else:
        #print("no need to press play")


def countdown(duration):
    for i in range(duration, 0, -1):
        print(f"Countdown: {i}         ", end='\r')
        time.sleep(1)
    print("Countdown: 0")

def check_ctrl_key():
    """Thread function to check for Ctrl key press."""
    while True:
        # Check if Ctrl key is pressed down; if so, exit the program immediately
        if win32api.GetAsyncKeyState(CTRL_KEY) & 0x8000:
            print("Ctrl key pressed. Exiting program immediately...")
            os._exit(0)  # Immediately terminate the program

def mainlogic():
    '''The  main logic of this wonderfull code'''
    loop_counter = 0
    max_counter = int(sys.argv[1])
    max_counter = max_counter // 7

    #determine which smurf windows are active
    active_smurf_windows = WindowsChecker.check_active_windows(all_smurf_windows)
    while loop_counter < max_counter:
        loop_counter+=1
        print("loop:", loop_counter, "of max:", max_counter)
        # click on create icon middle
        pyautogui.moveTo(2779, 193)
        time.sleep(0.2)
        pyautogui.click(button='left')
        time.sleep(0.5)

        # move to duister
        #pyautogui.moveTo(3106, 117)
        
        # move to red
        pyautogui.moveTo(2981, 121)

        # move to blue
        #pyautogui.moveTo(2869, 115)
        
        # move to green
        #pyautogui.moveTo(2752, 121)
        
        time.sleep(0.2)
        pyautogui.click(button='left')
        time.sleep(0.5)

        # click on sharf
        pyautogui.moveTo(2779, 193)
        time.sleep(0.2)
        pyautogui.click(button='left')
        time.sleep(0.5)

        # click on create icon left
        pyautogui.moveTo(2757, 191)
        time.sleep(0.2)
        pyautogui.click(button='left')
        countdown(20)  # * : takes 20 seconds realtime, gametime 10 sec????

        # click on recycle brown
        pyautogui.moveTo(3040, 310)
        time.sleep(0.2)
        pyautogui.click(button='left')
        time.sleep(0.5)
        
        # click on recycle green
        pyautogui.moveTo(2994, 313)
        time.sleep(0.2)
        pyautogui.click(button='left')
        time.sleep(0.5)
        



def main():
    """main function, starts a thread to check for ctrl_key pressand starts the main func"""
    if len(sys.argv) != 2:
        print("Usage: python beelden.py <counter in multiples of 7>")
        return


    ctrl_thread = threading.Thread(target=check_ctrl_key)
    ctrl_thread.daemon = True  # Set as a daemon so it won't prevent program exit
    ctrl_thread.start()
    mainlogic()

if __name__ == "__main__":
    main()
