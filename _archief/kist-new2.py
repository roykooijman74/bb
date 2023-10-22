import pyautogui
import time
import signal
from PIL import ImageGrab
from functools import partial

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

SMURFWINDOWS = [
    [2560, 0, 790, 460, 'Smurf 1'],
#    [3414, 0, 790, 460, 'Smurf 2'],
#    [4267, 0, 790, 460, 'Smurf 3'],
#    [2560, 461, 790, 460, 'Smurf 4'],
#    [3414, 461, 790, 460, 'Smurf 5'],
#    [4267, 461, 790, 460, 'Smurf 6'],
#    [2560, 921, 790, 460, 'Smurf 7'],
#    [3414, 921, 790, 460, 'Smurf 8'],
#    [4267, 921, 790, 460, 'Smurf 9'],
#    [1770, 0, 790, 460, 'Smurf 0'],
    [1770, 461, 790, 460, 'A Supersmurf'],
    [1770, 921, 790, 460, 'B MiniSmurf']
]

def enablectrlc():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None, wait=0.0):
    status = 0
    print("smurf roi's")
    for roi in rois:
        x1, y1, width, length, name = roi
        location = None
        #print(x1, y1, name)
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidencevalue, region=(x1, y1, width, length))
        except:
            pass

        if location:
            x = location[0]
            y = location[1] + offset
            pyautogui.moveTo(x, y)
            time.sleep(wait)
            pyautogui.click(button='left')
            status += 1
            print("=============================", x, y, status, image_path, name)
    return status

def drag_window(direction):
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0

    if direction == "up":
        start_x = 2880
        start_y = 200
        end_x = 2880
        end_y = 350
    elif direction == "down":
        start_x = 2880
        start_y = 350
        end_x = 2880
        end_y = 200
    elif direction == "left":
        start_x = 3200
        start_y = 222
        end_x = 2800
        end_y = 222
    elif direction == "right":
        start_x = 2800
        start_y = 222
        end_x = 3200
        end_y = 222

    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=2)
    pyautogui.mouseUp()
    time.sleep(0.3)

def main():
    enablectrlc()

    for _ in range(4):
        zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
        drag_window("up")

    drag_window("left")

    for _ in range(8):
        zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
        drag_window("down")

    drag_window("left")

    for _ in range(8):
        zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
        drag_window("up")

    drag_window("left")

    for _ in range(8):
        zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
        drag_window("down")
        

    for _ in range(4):
        drag_window("right")

    for _ in range(8):
        zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
        drag_window("up")

    drag_window("left")

    for _ in range(8):
        zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
        drag_window("down")

    drag_window("left")

    for _ in range(5):
        zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
        drag_window("up")


if __name__ == '__main__':
    false_counter = 0
    main()
