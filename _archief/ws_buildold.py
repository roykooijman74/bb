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


def zoek_offset(plaatje, offsetx, i):
    '''zoek offset function'''
    status = False
    imagex = 0
    imagey = 0
    try:
        imagex, imagey = pyautogui.locateCenterOnScreen(
            plaatje, confidence=0.8)  # type: ignore
    except pyautogui.ImageNotFoundException:
        status = False
        imagex = 0
        imagey = 0
    else:
        xpositie, ypositie = pyautogui.position()
        status = True
        pyautogui.moveTo(x=imagex+offsetx, y=imagey)
        time.sleep(0.1)
        pyautogui.click(button='left')
        pyautogui.moveTo(xpositie, ypositie)
    finally:
        print(i, status, imagex, imagey, plaatje)
    return


def main():
    '''main function'''

    enablectrlc()
    i = 0
    while True:
        i = i+1
        print("zoek v")
        zoek_offset(r"images\ws-place-ok.png", 0, i)
        time.sleep(0.1)
        if i == 5:
            pyautogui.moveTo(2635, 414)
            pyautogui.click(button='left')
            i = 0


if __name__ == '__main__':
    main()
