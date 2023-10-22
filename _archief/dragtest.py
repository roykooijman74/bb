import pyautogui
import time
import signal
from PIL import ImageGrab
from functools import partial

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

def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None, wait=0.0):
    status = 0
    print("start search")
    while True:  # Loop until no instances are found in any ROI
        found = False  # Flag to check if any instance was found in this iteration
        for roi in rois:
            x1, y1, width, length, name = roi
            x2 = x1 + 60
            y2 = y1 + 90
            width2= width - 60
            length2 = length - 110
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
        if not found:
            break  # If no instances were found in this iteration, exit the loop
    return status

#    [2560, 0, 790, 460, 'Smurf 1'],
start_x=2860
start_y=90
end_x=2860
end_y=360


# Move the mouse cursor to the starting position of the drag
pyautogui.moveTo(start_x, start_y)
#pyautogui.dragRel(0, 270, duration=3, button='left')
#pyautogui.dragRel(1, 1, duration=0, button='left')
#pyautogui.mouseUp()
pyautogui.mouseDown()
pyautogui.moveTo(end_x, end_y, duration=0.4)
#pyautogui.mouseUp()
#pyautogui.mouseDown()
pyautogui.moveTo(end_x, end_y, duration=0.4)
pyautogui.mouseUp()
#time.sleep(0.3)
status=zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)


pyautogui.moveTo(start_x, start_y)
#pyautogui.dragRel(0, 270, duration=3, button='left')
#pyautogui.dragRel(1, 1, duration=0, button='left')
#pyautogui.mouseUp()
pyautogui.mouseDown()
pyautogui.moveTo(end_x, end_y, duration=0.4)
#pyautogui.mouseUp()
#pyautogui.mouseDown()
pyautogui.moveTo(end_x, end_y, duration=0.4)
pyautogui.mouseUp()
status=zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
