'''python 3.11'''
import win32gui

SMURFWINDOWS = [
    [0, 0, 790, 460, 'Smurf 1']
]

# loop through windows and move/resize
for window in SMURFWINDOWS:
    print("zoeken naar: ", window[4])
    hwnd = win32gui.FindWindow(None, window[4])  # pylint: disable=I1101
    if hwnd:
        # get current window position and size
        _, _, win_width, win_height = win32gui.GetWindowRect(hwnd)  # pylint: disable=I1101
        # set new window position and size
        print("setting win: ", window[4])
        win_pos_x, win_pos_y, win_width_new, win_height_new = window[:4]
        # move window
        win32gui.SetWindowPos(   # pylint: disable=I1101
            hwnd, None, win_pos_x, win_pos_y,
            win_width_new, win_height_new, 0x0001)
        win32gui.SetWindowPos(   # pylint: disable=I1101
            hwnd, None, win_pos_x, win_pos_y,
            win_width_new, win_height_new, 0x0002 | 0x0040)
    else:
        print(f"Window '{window[4]}' not found.")
