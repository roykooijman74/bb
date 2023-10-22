import pyautogui
import time
import signal

SMURFWINDOWS = [
    [0, 0, 790, 460, 'Smurf 1'],
    [854, 0, 790, 460, 'Smurf 2'],
    [1707, 0, 790, 460, 'Smurf 3'],
    [0, 461, 790, 460, 'Smurf 4'],
    [854, 461, 790, 460, 'Smurf 5'],
    [1707, 461, 790, 460, 'Smurf 6'],
    [0, 921, 790, 460, 'Smurf 7'],
    [854, 921, 790, 460, 'Smurf 8'],
    [1707, 921, 790, 460, 'Smurf 9'],
    [-790, 0, 790, 460, 'Smurf 0'],
    [-790, 461, 790, 460, 'A Supersmurf'],
    [-790, 921, 790, 460, 'B MiniSmurf']
]

def enablectrlc():
    # KeyboardInterrupt: Ctrl-C
    # dependent on import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def get_initial_mouse_coordinates():
    return pyautogui.position()

def restore_mouse_coordinates(coordinates):
    pyautogui.moveTo(coordinates)

def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None):
    initial_mouse_coordinates = get_initial_mouse_coordinates()

    for roi in rois:
        x1, y1, width, length, name = roi
        x2 = x1 + width
        y2 = y1 + length
        location = None

        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidencevalue, region=(x1, y1, x2, y2))
        except:
            pass

        if location:
            x = location[0] #- 2560
            y = location[1] + offset
            pyautogui.moveTo(x, y)
            #time.sleep(0.2)
            pyautogui.click(button='left')
            #time.sleep(0.2)
            print(x,y,name,image_path)
            #time.sleep(0.5)

    restore_mouse_coordinates(initial_mouse_coordinates)

def main():
    enablectrlc()

    image_path = "images/npc-invasie.png"
    zoekplaatje(image_path, 70, rois=SMURFWINDOWS)
    image_path = "images/npc-vernietigen-bruin.png"
    zoekplaatje(image_path, 0, rois=SMURFWINDOWS)
    image_path = "images/npc-vernietigen-groen.png"
    zoekplaatje(image_path, 0, rois=SMURFWINDOWS)

if __name__ == '__main__':
    main()
