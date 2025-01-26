"""Python3.11"""
import time
from functools import partial
import pyautogui
from PIL import ImageGrab
import win32api
import win32con
import threading
import os

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

# Define the control key
CTRL_KEY = win32con.VK_CONTROL

SMURFWINDOWS = [
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


def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None, wait=0.3, loop=0, total=0):
    """zoekt plaatje in smurf windows"""
    if rois is None:
        rois = []
    status = 0
    loop+=1
    print("start search: ", loop)
    while True:  # Loop until no instances are found in any ROI
        found = False  # Flag to check if any instance was found in this iteration
        for roi in rois:
            x1, y1, width, length, name = roi
            x2 = x1 + 50
            y2 = y1 + 90
            width2 = width - 60
            length2 = length - 125
            location = None
            try:
                location = pyautogui.locateCenterOnScreen(
                    image_path,
                    confidence=confidencevalue,
                    region=(x2, y2, width2, length2),
                )  # type: ignore
            except pyautogui.ImageNotFoundException:
                pass
            if location:
                x = location[0]
                y = location[1] + offset
                pyautogui.moveTo(x, y)
                time.sleep(wait)
                pyautogui.click(button="left")
                status += 1
                total += 1

                found = True
                print("=============================", x, y, status, total, image_path, name)
        if not found:
            break  # If no instances were found in this iteration, exit the loop
    #total=total+status
    return status, loop, total


def starttopleftcorner():
    ''' start top left corner '''
    for _ in range(1, 4, 1):
        pyautogui.moveTo(2560 + 51, 0 + 90)
        pyautogui.mouseDown()
        pyautogui.moveTo(2560 + 615 + 51, 0 + 300 + 40, duration=1.0)
        pyautogui.mouseUp()
        pyautogui.mouseDown()
        pyautogui.moveTo(2560 + 615 + 51, 0 + 300 + 40, duration=0.2)
        pyautogui.mouseUp()


def down():
    ''' move down '''
    pyautogui.moveTo(2830, 390)
    pyautogui.mouseDown()
    pyautogui.moveTo(2830, 90, duration=0.8)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(2830, 90, duration=0.3)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(2830, 90, duration=0.3)
    pyautogui.mouseUp()
    pyautogui.moveTo(2966, 48)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.mouseUp()


def up():
    ''' move up '''
    pyautogui.moveTo(2830, 90)
    pyautogui.mouseDown()
    pyautogui.moveTo(2830, 390, duration=0.8)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(2830, 390, duration=0.3)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(2830, 390, duration=0.3)
    pyautogui.mouseUp()
    pyautogui.moveTo(2966, 48)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.mouseUp()


def right():
    ''' move to the right '''

    pyautogui.moveTo(2560 + 651, 240)
    pyautogui.mouseDown()
    pyautogui.moveTo(2560 + 51, 240, duration=1.1)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(2560 + 51, 240, duration=0.5)
    pyautogui.mouseUp()
    pyautogui.moveTo(2966, 48)
    pyautogui.moveTo(2560 + 51, 240, duration=0.5)
    pyautogui.mouseUp()
    pyautogui.moveTo(2966, 48)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.mouseUp()


def mainlogic():
    """main logic function"""
    total = 0
    loop=0
    starttopleftcorner()
    down()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    down()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    down()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    down()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    right()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    up()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    up()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    up()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    up()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    right()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    down()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    down()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    down()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    down()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    right()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    up()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    up()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    up()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    up()
    _, loop,total = zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8, loop=loop,total=total)
    
    print("ready searching chests, total:", total)
    pyautogui.moveTo(2560 + 21, 109)
    pyautogui.mouseDown()
    pyautogui.mouseUp()


    
    

def main():
    """main function, starts a thread to check for ctrl_key pressand starts the main func"""
    ctrl_thread = threading.Thread(target=check_ctrl_key)
    ctrl_thread.daemon = True  # Set as a daemon so it won't prevent program exit
    ctrl_thread.start()
    mainlogic()

if __name__ == "__main__":
    main()
