"""Python3.11"""
import signal
import time
from functools import partial

import pyautogui
from PIL import ImageGrab

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

SMURFWINDOWS = [
    [2560, 0, 790, 460, 'Smurf 1'],
    [3414, 0, 790, 460, 'Smurf 2'],
    [4267, 0, 790, 460, 'Smurf 3'],
    [2560, 461, 790, 460, 'Smurf 4'],
    [3414, 461, 790, 460, 'Smurf 5'],
    [4267, 461, 790, 460, 'Smurf 6'],
    [2560, 921, 790, 460, 'Smurf 7'],
    [3414, 921, 790, 460, 'Smurf 8'],
    [4267, 921, 790, 460, 'Smurf 9'],
    [1770, 0, 790, 460, 'Smurf 0'],
    [1770, 461, 790, 460, 'A Supersmurf'],
    [1770, 921, 790, 460, 'B MiniSmurf']
]


def enablectrlc():
    '''enable ctrl-c'''
    signal.signal(signal.SIGINT, signal.SIG_DFL)


def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None, wait=0.1):
    '''zoekplaat'''
    location = []
    status = 0
    for roi in rois:
        x1, y1, width, length, name = roi
        location = None
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidencevalue,
                                                      region=(x1, y1, width, length))
        except pyautogui.ImageNotFoundException:
            pass

        if location:
            x = location[0]
            y = location[1] + offset
            pyautogui.moveTo(x, y)
            time.sleep(wait)
            pyautogui.click(button='left')
            status = status + 1
            print("=============================", x, y, status, image_path, name)
    return status


def main():
    '''main function'''
    enablectrlc()
    x = 80
    for y in range(80, 440, 30):
        pyautogui.moveTo(2670, y)
        time.sleep(0.1)
        pyautogui.click(button='left')
        time.sleep(0.3)
        print("====Searching for invasie")
        roiok = []
        for roi in SMURFWINDOWS:
            x1, y1, width, length, _ = roi
            if pyautogui.locateOnScreen("images/npc-invasie2.png", confidence=0.7,
                                        region=(x1, y1, width, length)):
                roiok.append(roi)

        if roiok:
            status = zoekplaatje("images/npc-invasie2.png", 70, rois=roiok, wait=0.5)
            if status > 0:
                print("====Bruin")
                time.sleep(0.1)
                zoekplaatje("images/npc-vernietigen-bruin.png", 0, rois=roiok, wait=0)
                time.sleep(0.6)
                print("====Groen")
                zoekplaatje("images/npc-vernietigen-groen.png", 0, rois=roiok, wait=0)
            roiok = []

    print("====Ready")

    pyautogui.moveTo(2759, 44)
    time.sleep(0.1)
    pyautogui.click(button='left')


if __name__ == '__main__':
    main()
