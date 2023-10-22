import pyautogui
import time
import signal
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

SMURFWINDOWS = [
    [2560, 0, 790, 460, 'Smurf 1'],
    # [3414, 0, 790, 460, 'Smurf 2'],
    # [4267, 0, 790, 460, 'Smurf 3'],
    # [2560, 461, 790, 460, 'Smurf 4'],
    # [3414, 461, 790, 460, 'Smurf 5'],
    # [4267, 461, 790, 460, 'Smurf 6'],
    # [2560, 921, 790, 460, 'Smurf 7'],
    # [3414, 921, 790, 460, 'Smurf 8'],
    # [4267, 921, 790, 460, 'Smurf 9'],
    [1770, 0, 790, 460, 'Smurf 0'],
    # [1770, 461, 790, 460, 'A Supersmurf'],
    [1770, 921, 790, 460, 'B MiniSmurf']
]

def enablectrlc():
    # KeyboardInterrupt: Ctrl-C
    # dependent on import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None, wait=0.0):
    status = 0
    print("start search")
    found = False
    for roi in rois[:]:  # Use a copy of the list
        x1, y1, width, length, name = roi
        x2 = x1
        y2 = y1
        width2 = width
        length2 = length
        location = None
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidencevalue, region=(x2, y2, width2, length2))
        except:
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

            # Remove the window from the list after clicking
#                rois.remove(roi)
#                print(rois)

    return status

def main():
    enablectrlc()
    status = 3
    while True:
        print(status)
        #print("Searching for start-gelukttest.png")
        aantal = zoekplaatje("images/start-gelukttest.png", rois=SMURFWINDOWS)
        status = status - aantal
        if status == 0:
            print("No more instances of start-gelukttest.png found.")
            break

if __name__ == '__main__':
    main()
