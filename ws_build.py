"""Python3.11"""
import signal
import time
from functools import partial
import os
import sys
import pyautogui
from PIL import ImageGrab

import threading
import win32api
import win32con

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

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
        CTRL_KEY = win32con.VK_CONTROL
        while True:
            # Check if Ctrl key is pressed down; if so, exit the program immediately
            if win32api.GetAsyncKeyState(CTRL_KEY) & 0x8000:
                print("Ctrl key pressed. Exiting program immediately...")
                os._exit(0)  # Immediately terminate the program


def enablectrlc():
    '''enable ctrl-c'''
    signal.signal(signal.SIGINT, signal.SIG_DFL)


def zoekplaatje(image_path, offset=0, confidencevalue=0.6, wait=0.1):
    imagex = 0
    imagey = 0
    location = []
    status = 0
    print("searching for ",image_path)

    try:
        location = pyautogui.locateCenterOnScreen(
            image_path, confidence=confidencevalue)  # type: ignore
    except pyautogui.ImageNotFoundException:
        print("not found")
        pass
        

    if location:
        x = location[0]
        y = location[1] + offset
        pyautogui.moveTo(x, y)
        time.sleep(wait)
        pyautogui.click(button='left')
        status = status + 1
        print("=============================", x, y, status, image_path)
    return status



def main():
    '''main function'''
    """main function, starts a thread to check for ctrl_key pressand starts the main func"""
    ctrl_thread = threading.Thread(target=GenericHelpers.check_ctrl_key)
    ctrl_thread.daemon = True  # Set as a daemon so it won't prevent program exit
    ctrl_thread.start()

#    enablectrlc()
    i = 0
    while True:
        i = i+1
        print("zoek v")
        zoekplaatje(r"images\ws-place-ok2.png", 0)
        time.sleep(0.5)
        if i == 2:
            pyautogui.moveTo(2635, 414)
            pyautogui.click(button='left')
            i = 0


if __name__ == '__main__':
    main()
