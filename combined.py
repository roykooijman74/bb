''' my python code for automating boring stuff in boom beach'''
import sys
import time
from functools import partial
import win32gui
import pyautogui
from PIL import ImageGrab
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
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
    [1770, 0, 790, 460, 'A Supersmurf'],
    [1770, 461, 790, 460, 'B MiniSmurf'],
    [1770, 921, 790, 460, 'C KickSmurf'],
]

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
    pyautogui.moveTo(2560+465,14)
    item = [465, 14, 247, 250, 255, "pauze button"]
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
    pyautogui.moveTo(2560+465,14)
    item = [461, 18, 247, 250, 255, "start button"]
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
    npc_counter = 0

    #determine which smurf windows are active
    active_smurf_windows = WindowsChecker.check_active_windows(all_smurf_windows)

    for y in range(80, 120, 30):
        pyautogui.moveTo(2670, y)
        pyautogui.click(button='left')

    time.sleep(0.2)

    #for y in range(80, 440, 30):
    for y in range(80, 440, 30):
        start_the_play_button(active_smurf_windows)
        # * move to menu position
        pyautogui.moveTo(2670, y)
        time.sleep(0.2)
        pyautogui.click(button='left')
        time.sleep(1.8)
        loop_counter += 1
        pause_the_play_button(active_smurf_windows)

        #check if everything is ready to start, if not exit
#        print("checking if everything is ok to start")

        for smurf in active_smurf_windows:
            item = [30, 74, 95, 184, 229, "player level icon"]
            status, smurf = zoek_item_on_color(item, smurf)
            if status:
                print(item[5], "found for ", smurf, "exiting as that shouldnt be visible")
                sys.exit()


        print("======= Searching for invasion:", loop_counter)
        for smurf in active_smurf_windows:
            # * reward check code
            #item = [450, 316, 151, 157, 142, "reward"]
            item = [448, 315, 255, 255, 254, "reward"]
            status, smurf = zoek_item_on_color(item, smurf)
            if status:
                click_on_screen_for_smurf(smurf,item[0],item[1])
                print(item[5], "found for ", smurf)

            # # * invasion middle code
            # item = [415, 189, 43, 43, 53, "invasion middle"]   #2560+415=2975 
            # status, smurf = zoek_item_on_color(item, smurf)
            # if status:
            #     click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=64, offset_y=69)
            #     npc_counter+=1
            #     print(item[5], "found for ", smurf, "counter = ",npc_counter)
            #     time.sleep(0.3)
            #     #click brown position
            #     pyautogui.moveTo(smurf[0] + 525, smurf[1] + 209)
            #     pyautogui.click(button='left')
            #     time.sleep(0.5)
            #     #click green position
            #     pyautogui.moveTo(smurf[0] + 430, smurf[1] + 320)
            #     pyautogui.click(button='left')

            # # * invasion left code
            # item = [274, 190, 65, 64, 71, "invasion left"]
            # status, smurf = zoek_item_on_color(item, smurf)
            # if status:
            #     click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=-75, offset_y=58)
            #     npc_counter+=1
            #     print(item[5], "found for ", smurf, "counter = ",npc_counter)
            #     time.sleep(0.3)
            #     #click brown position
            #     pyautogui.moveTo(smurf[0] + 350, smurf[1] + 212)
            #     pyautogui.click(button='left')
            #     time.sleep(0.5)
            #     #click green position
            #     pyautogui.moveTo(smurf[0] + 430, smurf[1] + 320)
            #     pyautogui.click(button='left')


        # GOLD CHECK        
        for smurf in active_smurf_windows:
            falsegold=True
            while falsegold:
                item = [406, 46, 82, 67, 0, "gold grayed out"]
                status, smurf = zoek_item_on_color(item, smurf)
                if status:
                    print(item[5], "found for ", smurf)
                    click_on_screen_for_smurf(smurf,item[0],item[1])
                    time.sleep(0.2)
                else:
                    falsegold=False



    print("====Ready")
    start_the_play_button(active_smurf_windows)
    pyautogui.moveTo(2759, 44)
    time.sleep(0.5)
    pyautogui.click(button='left')


def main():
    """main function, starts a thread to check for ctrl_key pressand starts the main func"""
    ctrl_thread = threading.Thread(target=check_ctrl_key)
    ctrl_thread.daemon = True  # Set as a daemon so it won't prevent program exit
    ctrl_thread.start()
    mainlogic()

if __name__ == "__main__":
    main()
