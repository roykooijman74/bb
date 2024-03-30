'''python 3.11'''
from logging import root
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
    if rois is None:
        rois = []
    for roi in rois:
        x1, y1, width, length, name = roi
        location = None
        try:
            location = pyautogui.locateCenterOnScreen(
                image_path, confidence=confidencevalue, region=(x1, y1, width, length))  # type: ignore
        except pyautogui.ImageNotFoundException:
            pass

        if location:
            x = location[0]
            y = location[1] + offset
            pyautogui.moveTo(x, y)
            time.sleep(wait)
            pyautogui.click(button='left')
            status = status + 1
            print(name, "vernietigen", x, y)
    return status,x,y




def main():
    '''main function'''
    enablectrlc()
    #vernietigen_smurfs = []  # List to store smurf names found during "vernietigen" search

    for y in range(80, 440, 30):
        pyautogui.moveTo(2670, y)
        time.sleep(0.2)
        pyautogui.click(button='left')
        time.sleep(1.8)
        print("=======  Searching for invasie")
        roiok = []
        for roi in SMURFWINDOWS:
            x1, y1, width, length, name = roi
            if pyautogui.locateOnScreen("images/npc-invasie2.png", confidence=0.7,
                                        region=(x1, y1, width, length)):
                roiok.append(roi)

        print(roiok)
        if roiok:
            status,xfound,yfound = zoekplaatje("images/npc-invasie2.png", 70, rois=roiok, wait=0.1)
            if status > 0:
                for smurf_info in roiok:
                    _, _, _, _, smurf_name = smurf_info
                    #vernietigen_smurfs.append(smurf_name)
            if len(roiok) == 1:
                time.sleep(2.0)
            else:
                time.sleep(0.3)
            
            for smurf_info in roiok:
                x1, y1, _, _, _ = smurf_info
 #               print(smurf_info[4], "brown",x1,"diff ",x1-478)
                x, y = x1 + 478, y1 + 206  # Brown coordinates relative to x1, y1

                xtest= xfound -x1
                ytest= yfound -y1
                print(smurf_info[4],xtest,ytest)
                pyautogui.moveTo(x, y)
#                pyautogui.click(button='left')
                if len(roiok) == 1:
                    time.sleep(1.0)
                else:
                    time.sleep(0.3)
            time.sleep(0.6)

            for smurf_info in roiok:
                x1, y1, _, _, _ = smurf_info
                x, y = x1 + 433, y1 + 310  # Green coordinates relative to x1, y1
#                print(smurf_info[4], "green",x,y,x1,y1,smurf_info[0]-x1,smurf_info[2]-y1)
                pyautogui.moveTo(x, y)
                if len(roiok) == 1:
                    time.sleep(1.0)
                else:
                    time.sleep(0.3)
            time.sleep(0.6)
    print("====Ready")

    pyautogui.moveTo(2759, 44)
    time.sleep(0.5)
    pyautogui.click(button='left')


if __name__ == '__main__':
    main()
