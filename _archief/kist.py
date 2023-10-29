"""Python3.11"""
import time
import signal
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


def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None, wait=0.0):
    '''zoekt plaatje in smurf windows'''
    if rois is None:
        rois = []
    status = 0
    print("start search")
    while True:  # Loop until no instances are found in any ROI
        found = False  # Flag to check if any instance was found in this iteration
        for roi in rois:
            x1, y1, width, length, name = roi
            x2 = x1 + 60
            y2 = y1 + 90
            width2 = width - 60
            length2 = length - 110
            location = None
            try:
                location = pyautogui.locateCenterOnScreen(image_path,
                                                          confidence=confidencevalue,
                                                          region=(x2, y2,
                                                                  width2, length2))  # type: ignore
            except pyautogui.ImageNotFoundException:
                pass
            if location:
                x = location[0]
                y = location[1] + offset
                pyautogui.moveTo(x, y)
                time.sleep(wait)
                pyautogui.click(button='left')
                status += 1
                found = True
                print("=============================", x, y, status, image_path, name)
        if not found:
            break  # If no instances were found in this iteration, exit the loop
    return status


def drag_window(direction):
    '''drag smurf windows'''
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    duration = 0.1
    if direction == "up":
        start_x = 2880
        start_y = 100
        end_x = 2880
        end_y = 385
        duration = 0.4
    elif direction == "down":
        start_x = 2880
        start_y = 385
        end_x = 2880
        end_y = 100
        duration = 0.4
    elif direction == "left":
        start_x = 3200
        start_y = 222
        end_x = 2800
        end_y = 222
        duration = 0.7
    elif direction == "right":
        start_x = 2800
        start_y = 222
        end_x = 3200
        end_y = 222
        duration = 0.7

    print("dragging : ", direction)
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=duration)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=0.1)
    pyautogui.mouseUp()
    pyautogui.moveTo(2966, 48)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.mouseUp()


def main():
    '''main function'''
    enablectrlc()

    for _ in range(3):
        zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8)
        drag_window("up")

    drag_window("left")

    for _ in range(4):
        zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8)
        drag_window("down")

    drag_window("left")

    for _ in range(5):
        zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8)
        drag_window("up")

    drag_window("left")

    for _ in range(5):
        drag_window("down")

    for _ in range(4):
        drag_window("right")

    for _ in range(5):
        zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8)
        drag_window("up")

    drag_window("left")

    for _ in range(5):
        zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8)
        drag_window("down")

    drag_window("left")

    for _ in range(3):
        zoekplaatje(r"images\kistje.png", 0, rois=SMURFWINDOWS, confidencevalue=0.8)
        drag_window("up")


if __name__ == '__main__':
    main()
