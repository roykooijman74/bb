import pyautogui
import time
import signal
import pyttsx3
from PIL import ImageGrab
from functools import partial

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

SMURFWINDOWS=[
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
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None, wait=0.0):
    status=0
    for roi in rois:
        x1, y1, width, length, name = roi
        #x2 = x1 + width
        #y2 = y1 + length
        location = None
        print(x1,y1,name)
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
            status=status+1
            #time.sleep(0.2)
            print("=============================", x, y, status, image_path, name)
    return status


def drag_down():
    # Define the coordinates of the starting and ending positions
    start_x = 2880
    start_y = 200
    end_x = 2880
    end_y = 350
    duration = 3
    # Move the mouse cursor to the starting position
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    # Move the mouse to the ending position (dragging the window)
    pyautogui.moveTo(end_x, end_y, duration=duration)
    pyautogui.mouseUp()
    time.sleep(0.2)

def drag_up():
    # Define the coordinates of the starting and ending positions
    start_x = 2880
    start_y = 350
    end_x = 2880
    end_y = 200
    duration = 3
    # Move the mouse cursor to the starting position
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    # Move the mouse to the ending position (dragging the window)
    pyautogui.moveTo(end_x, end_y, duration=duration)
    pyautogui.mouseUp()
    time.sleep(0.2)


def drag_left():
    # Define the coordinates of the starting and ending positions
    start_x = 3100
    start_y = 222
    end_x = 2800
    end_y = 222
    duration = 3
    # Move the mouse cursor to the starting position
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    # Move the mouse to the ending position (dragging the window)
    pyautogui.moveTo(end_x, end_y, duration=duration)
    pyautogui.mouseUp()
    time.sleep(0.2)

def drag_right():
    # Define the coordinates of the starting and ending positions
    start_x = 2800
    start_y = 222
    end_x = 3100
    end_y = 222
    duration = 3
    # Move the mouse cursor to the starting position
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    # Move the mouse to the ending position (dragging the window)
    pyautogui.moveTo(end_x, end_y, duration=duration)
    pyautogui.mouseUp()
    time.sleep(0.2)


def main():
    enablectrlc()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)

    drag_left()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    
    drag_left()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)

    
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
 
    drag_right()
    drag_right()
    drag_right()
    drag_right()
    drag_right()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)

    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)

    drag_left()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)

    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_up()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
 
    drag_left()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)

    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)
    drag_down()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)




if __name__ == '__main__':
    false_counter=0
    main()
