import signal
import time
from functools import partial
import pyautogui
from PIL import ImageGrab

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

SMURFWINDOWS = [
    [3414, 0, 790, 460, 'Smurf 2'],
    [4267, 0, 790, 460, 'Smurf 3'],
    [2560, 461, 790, 460, 'Smurf 4'],
    [3414, 461, 790, 460, 'Smurf 5'],
    [4267, 461, 790, 460, 'Smurf 6'],
    [2560, 921, 790, 460, 'Smurf 7'],
    [3414, 921, 790, 460, 'Smurf 8'],
    [4267, 921, 790, 460, 'Smurf 9'],
    [1770, 0, 790, 460, 'A Supersmurf'],
    [1770, 461, 790, 460, 'B MiniSmurf'],
    [1770, 921, 790, 460, 'C KickSmurf'],
]

def enable_ctrl_c():
    '''Enable Ctrl-C interruption'''
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def search_image(image_path, npcteller, offset=0, confidencevalue=0.7, rois=None, wait=0.1):
    '''Search for an image within specified regions of interest (ROIs)'''
    rois = rois or []
    status, found_x, found_y = 0, None, None

    for roi in rois:
        x1, y1, width, length, name = roi
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidencevalue, region=(x1, y1, width, length))

        if location:
            x, y = location[0], location[1] + offset
            pyautogui.moveTo(x, y)
            time.sleep(wait)
            pyautogui.click(button='left')
            status += 1
            print(npcteller, name, "destroyed at", x, y)
            npcteller += 1
            found_x, found_y = x, y

    return npcteller, status, found_x, found_y

def main():
    '''Main function'''
    enable_ctrl_c()
    loop_counter, npc_counter = 0, 1

    for y in range(80, 440, 30):
        pyautogui.moveTo(2670, y)
        time.sleep(0.2)
        pyautogui.click(button='left')
        time.sleep(1.8)
        loop_counter += 1
        print("======= Searching for invasion:", loop_counter)

        valid_rois = [roi for roi in SMURFWINDOWS if pyautogui.locateOnScreen("images/npc-invasie2.png", confidence=0.7, region=(roi[0], roi[1], roi[2], roi[3]))]

        if valid_rois:
            npc_counter, status, found_x, found_y = search_image("images/npc-invasie2.png", npc_counter, 70, rois=valid_rois, wait=0.1)

            if status > 0:
                for smurf_info in valid_rois:
                    x1, y1, _, _, smurf_name = smurf_info
                    #print(smurf_name, "detected at", found_x, found_y)

            sleep_time = 1.5 if len(valid_rois) == 1 else 1.3
            time.sleep(sleep_time)

            for smurf_info in valid_rois:
                x1, y1 = smurf_info[:2]
                brown_coords = (x1 + 498, y1 + 206)
                for coords in [brown_coords]:
                    pyautogui.moveTo(*coords)
                    pyautogui.click(button='left')
                    time.sleep(0.2)
            time.sleep(sleep_time)

            for smurf_info in valid_rois:
                x1, y1 = smurf_info[:2]
                green_coords = (x1 + 433, y1 + 310)
                for coords in [green_coords]:
                    pyautogui.moveTo(*coords)
                    pyautogui.click(button='left')
                    time.sleep(0.2)

    print("====Ready")
    pyautogui.moveTo(2759, 44)
    time.sleep(0.5)
    pyautogui.click(button='left')

if __name__ == '__main__':
    main()
