''' my own grab and check it code '''
import time
import os
import argparse
from functools import partial
import threading
import win32api
import pyautogui
from PIL import Image, ImageGrab
from tabulate import tabulate
import win32gui
import win32con

# Configure ImageGrab to grab from all screens
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


CTRL_KEY = win32con.VK_CONTROL

# List of all windows (Smurfs) with coordinates and names
all_smurf_windows = [
    [2560, 0, 790, 460, "Smurf 1"],
    [3414, 0, 790, 460, "Smurf 2"],
    [4267, 0, 790, 460, "Smurf 3"],
    [2560, 461, 790, 460, "Smurf 4"],
    [3414, 461, 790, 460, "Smurf 5"],
    [4267, 461, 790, 460, "Smurf 6"],
    [2560, 921, 790, 460, "Smurf 7"],
    [3414, 921, 790, 460, "Smurf 8"],
    [4267, 921, 790, 460, "Smurf 9"],
    [1770, 0, 790, 460, "A Supersmurf"],
    [1770, 461, 790, 460, "B MiniSmurf"],
    [1770, 921, 790, 460, "C KickSmurf"],
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
    def find_window_by_position(x, y):
        for window in all_smurf_windows:
            win_x, win_y, width, height, name = window
            if win_x <= x < win_x + width and win_y <= y < win_y + height:
                return window
        return None


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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def set_smurf_windows_positions(active_smurf_windows):
        for window in active_smurf_windows:
            print("zoeken naar: ", window[4])
            hwnd = win32gui.FindWindow(None, window[4])  # pylint: disable=I1101
            if hwnd:
                # get current window position and size
                _, _, win_width, win_height = win32gui.GetWindowRect(hwnd)  # pylint: disable=I1101
                # set new window position and size
                print("setting win: ", window[4])
                win_pos_x, win_pos_y, win_width_new, win_height_new = window[:4]
                # move window
                win32gui.SetWindowPos(   # pylint: disable=I1101
                    hwnd, None, win_pos_x, win_pos_y,
                    win_width_new, win_height_new, 0x0001)
                win32gui.SetWindowPos(   # pylint: disable=I1101
                    hwnd, None, win_pos_x, win_pos_y,
                    win_width_new, win_height_new, 0x0002 | 0x0040)
            else:
                print(f"Window '{window[4]}' not found.")



class BlueStacksHelper:
    """Defines functions for checking Bluestacks action button."""

    @staticmethod
    def pause_the_play_button(active_smurf_windows):
        '''The play button will be pauzed'''
        pyautogui.moveTo(2560+465,14)
        item = [465, 14, 247, 250, 255, "pauze button"]
        status, smurf = WindowsChecker.zoek_item_on_color(item, active_smurf_windows[0])
        if status:
            click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=0, offset_y=0)
            #print("pauze pressed")
        #else:
            #print("no need to press pauze")

    @staticmethod
    def start_the_play_button(active_smurf_windows):
        '''The play button will be started'''
        # ensure play/pause button is pauzed
        #move to pauze location to highligth the button
        pyautogui.moveTo(2560+465,14)
        item = [461, 18, 247, 250, 255, "start button"]
        status, smurf = WindowsChecker.zoek_item_on_color(item, active_smurf_windows[0])
        if status:
            click_on_screen_for_smurf(smurf,item[0],item[1],offset_x=0, offset_y=0)
            #        print("play pressed")
        #else:
            #print("no need to press play")

class GenericHelpers:

    @staticmethod
    def countdown(duration):
        for i in range(duration, 0, -1):
            print(f"Countdown: {i}         ", end='\r')
            time.sleep(1)
        print("Countdown: 0")

    @staticmethod
    def check_ctrl_key():
        """Thread function to check for Ctrl key press."""
        while True:
            # Check if Ctrl key is pressed down; if so, exit the program immediately
            if win32api.GetAsyncKeyState(CTRL_KEY) & 0x8000:
                print("Ctrl key pressed. Exiting program immediately...")
                os._exit(0)  # Immediately terminate the program

def capture_image(x, y, length, height, image_name):
    # Define the region to capture (left, top, right, bottom)
    region = (x, y, x + length, y + height)

    # Capture the region
    screenshot = ImageGrab.grab(bbox=region)

    # Ensure the 'captured_images' directory exists
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)

    # Save the captured image
    captured_image_path = os.path.join(output_dir, image_name)
    screenshot.save(captured_image_path)
    print(f"Captured image saved at: {captured_image_path}")



def mainlogic():
    '''main logic of the program.'''
    #get arguments parsed to this program
    parser = argparse.ArgumentParser(description="Capture a region of the screen based on mouse position.")
    parser.add_argument("length", type=int, help="The length of the region to capture.")
    parser.add_argument("height", type=int, help="The height of the region to capture.")
    parser.add_argument("imagename", type=str, help="The name of the output image file (e.g., 'image.png').")
    args = parser.parse_args()

    #determine which smurf windows are active
    active_smurf_windows = WindowsChecker.check_active_windows(all_smurf_windows)

    #set windows to correct position
    WindowsChecker.set_smurf_windows_positions(active_smurf_windows)


    # Identify the window containing the mouse position
    x, y = pyautogui.position()
    print(f"Mouse position: x={x}, y={y}")
    window = WindowsChecker.find_window_by_position(x, y)
    if window:
        win_x, win_y, _, _, win_name = window
        rel_x, rel_y = x - win_x, y - win_y
        print(f"Mouse window: {win_name}")
        print(f"Relative position: x={rel_x}, y={rel_y}")
    else:
        print("Mouse is not within any defined window.")
        exit()

    capture_image(x, y, args.length, args.height, args.imagename)
    
    output_dir = "images"
    for smurf in active_smurf_windows:
        x1, y1, width, length, name = smurf
        x2=x1+rel_x
        y2=y1+rel_y
        
        location = None
        image_path = os.path.join(output_dir, args.imagename)

        confidencevalue=0.6
        
        try:
            location = pyautogui.locateCenterOnScreen(
                image_path,
                confidence=confidencevalue,
                region=(x2, y2, args.length, args.height),
            )  # type: ignore
        except pyautogui.ImageNotFoundException:
            pass
        if location:
            # x = location[0]
            # y = location[1] + offset
            # pyautogui.moveTo(x, y)
            # time.sleep(wait)
            # pyautogui.click(button="left")
            # status += 1
            print("=============================", x, y, location, image_path, name)
        else:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX", x, y, location, image_path, name)

    print("item: ", rel_x, ",", rel_y, ",", args.length, "," , args.height, ",", args.imagename)





def main():

    """main function, starts a thread to check for ctrl_key pressand starts the main func"""
    ctrl_thread = threading.Thread(target=GenericHelpers.check_ctrl_key)
    ctrl_thread.daemon = True  # Set as a daemon so it won't prevent program exit
    ctrl_thread.start()
    mainlogic()

if __name__ == "__main__":
    main()

