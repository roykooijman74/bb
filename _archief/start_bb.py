"""Python3.11"""
import signal
import time
from functools import partial

import pyautogui
import win32gui
from PIL import ImageGrab

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

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
    [1770, 0, 790, 460, "Smurf 0"],
    [1770, 461, 790, 460, "A Supersmurf"],
    [1770, 921, 790, 460, "B MiniSmurf"],
]


def enablectrlc():
    """enable ctrl-c"""
    signal.signal(signal.SIGINT, signal.SIG_DFL)


def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None, wait=0.0):
    """zoekplaat met region"""
    status = 0
    if rois is not None:
        for roi in rois:
            x1, y1, width, length, name = roi
            print("searching for ", name)
            location = None
            try:
                location = pyautogui.locateCenterOnScreen(
                    image_path,
                    confidence=confidencevalue,
                    region=(x1, y1, width, length),
                )  # type: ignore
            except pyautogui.ImageNotFoundException:
                pass

            if location:
                x, y = location[0], location[1] + offset
                pyautogui.moveTo(x, y)
                time.sleep(wait)
                pyautogui.click(button="left")
                status += 1
                print("=============================", x, y, status, image_path, name)

    return status


def fixmulti():
    """fix the multi instance manager window postion"""
    # BlueStacks Multi Instance Manager: (1084, 707), 692 x 687
    hwnd = win32gui.FindWindow(None, "BlueStacks Multi Instance Manager")  # pylint: disable=I1101
    if hwnd:
        win_pos_x, win_pos_y, win_width_new, win_height_new = [1084, 707, 695, 687]
        win32gui.SetWindowPos(  # pylint: disable=I1101
            hwnd, None, win_pos_x, win_pos_y, win_width_new, win_height_new, 0x0001
        )
        win32gui.SetWindowPos(  # pylint: disable=I1101
            hwnd,
            None,
            win_pos_x,
            win_pos_y,
            win_width_new,
            win_height_new,
            0x0002 | 0x0040,
        )
        win32gui.SetForegroundWindow(hwnd)  # pylint: disable=I1101
    else:
        print("Window not found.")


def zoekplaatjesimpel(plaatje, offset=0, confidencevalue=0.9):
    """zoekplaat zonder region"""
    location = None
    imagex = 0
    imagey = 0

    try:
        location = pyautogui.locateCenterOnScreen(plaatje, confidence=confidencevalue)  # type: ignore
        print(location)
    except pyautogui.ImageNotFoundException:
        status = False
    else:
        x = location[0]
        y = location[1] + offset
        status = True
        x = imagex  # -2560
        y = imagey + offset
        pyautogui.moveTo(x, y)
        pyautogui.click(button="left")
        print("found", plaatje)
    return status, imagex, imagey


def main():
    """main function"""

    enablectrlc()
    fixmulti()
    #    fixtask()
    total_instances = len(SMURFWINDOWS)
    print(total_instances)
    while total_instances > 0:
        # print("searching android start")
        # zoekplaatjesimpel("images/start-android.png")
        print("searching boombeach app start")
        zoekplaatje("images/start-boombeach.png", rois=SMURFWINDOWS)
        time.sleep(0.5)
        print("Remaining instances to find:", total_instances)
        instances_found = zoekplaatje("images/start-gelukttest.png", rois=SMURFWINDOWS)
        total_instances -= instances_found

    print("No more instances of start-gelukttest.png found.")


if __name__ == "__main__":
    main()
