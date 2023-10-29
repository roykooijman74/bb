"""Module providing a function to wait for a bit."""
import time
import pyautogui
import win32con
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

# loop through windows and move/resize
for window in SMURFWINDOWS:
    hwnd = win32gui.FindWindow(None, window[4])  # find the window # pylint: disable=I1101
    if hwnd:
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)  # close the window # pylint: disable=I1101
        print(window, window[0]+500, window[1]+270)
        # close = x+ 500  en windowshift = -2560)
        pyautogui.moveTo(window[0]+500, window[1]+270)
        pyautogui.click(button='left')

    else:
        print(f"Window '{window[4]}' not found.")

time.sleep(1.0)
