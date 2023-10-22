import pyautogui
import time
import signal
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import win32gui

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
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None, wait=0.0):
    status = 0
    found = False
    for roi in rois:
        x1, y1, width, length, name = roi
        print("searching for " , name)
        location = None
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidencevalue, region=(x1, y1, width, length))
        except:
            pass

        if location:
            x, y = location[0], location[1] + offset
            pyautogui.moveTo(x, y)
            time.sleep(wait)
            pyautogui.click(button='left')
            status += 1
            found = True
            print("=============================", x, y, status, image_path, name)

    return status

def fixmulti():
#BlueStacks Multi Instance Manager: (1084, 707), 692 x 687
    hwnd = win32gui.FindWindow(None, "BlueStacks Multi Instance Manager")
    if hwnd:
         # get current window position and size
         _, _, win_width, win_height = win32gui.GetWindowRect(hwnd)
         # set new window position and size
         win_pos_x, win_pos_y, win_width_new, win_height_new = [1084, 707, 695, 687]
         # move window
         win32gui.SetWindowPos(hwnd, None, win_pos_x, win_pos_y, win_width_new, win_height_new, 0x0001)
         # resize window
         win32gui.SetWindowPos(hwnd, None, win_pos_x, win_pos_y, win_width_new, win_height_new, 0x0002 | 0x0040)
         # Bring the window to the front
         win32gui.SetForegroundWindow(hwnd)
    else:
            print(f"Window '{window[4]}' not found.")


def fixtask():
#Taakbeheer: (1092, 0), 678 x 727
    hwnd = win32gui.FindWindow(None, "Taakbeheer")
    if hwnd:
         # get current window position and size
         _, _, win_width, win_height = win32gui.GetWindowRect(hwnd)
         # set new window position and size
         win_pos_x, win_pos_y, win_width_new, win_height_new = [1084, 0, 695, 727]
         # move window
         win32gui.SetWindowPos(hwnd, None, win_pos_x, win_pos_y, win_width_new, win_height_new, 0x0001)
         # resize window
         win32gui.SetWindowPos(hwnd, None, win_pos_x, win_pos_y, win_width_new, win_height_new, 0x0002 | 0x0040)
         # Bring the window to the front
         win32gui.SetForegroundWindow(hwnd)
    else:
            print(f"Window '{window[4]}' not found.")


def zoekplaatjesimpel(plaatje,offset=0,confidencevalue=0.9):
    xpositie,ypositie=pyautogui.position()
    try:
        imagex,imagey = pyautogui.locateCenterOnScreen(plaatje, confidence=confidencevalue)
    except:
        status=False
        imagex=0
        imagey=0
    else:
        status=True
        x=imagex#-2560
        y=imagey+offset
        pyautogui.moveTo(x,y)
        pyautogui.click(button='left')
        print("found",plaatje)
    finally:
        return status,imagex,imagey


def main():
    enablectrlc()
    fixmulti()
#    fixtask()
    total_instances = len(SMURFWINDOWS)
    print(total_instances)
    while total_instances > 0:
        print("searching android start")
        zoekplaatjesimpel("images/start-android.png")
        print("searching boombeach app start")
        zoekplaatje("images/start-boombeach.png",rois=SMURFWINDOWS)
        time.sleep(0.5)
        print("Remaining instances to find:", total_instances)
        instances_found = zoekplaatje("images/start-gelukttest.png", rois=SMURFWINDOWS)
        total_instances -= instances_found


    print("No more instances of start-gelukttest.png found.")

if __name__ == '__main__':
    main()
