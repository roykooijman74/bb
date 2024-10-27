"""Python3.11"""
import signal
import time
from functools import partial

import pyautogui
from PIL import ImageGrab

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


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

    enablectrlc()
    i = 0
    while True:
        i = i+1
        print("zoek v")
        zoekplaatje(r"images\ws-place-ok.png", 0)
        time.sleep(0.5)
        if i == 5:
            pyautogui.moveTo(2635, 414)
            pyautogui.click(button='left')
            i = 0


if __name__ == '__main__':
    main()
