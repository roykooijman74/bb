'''python 3.11'''
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
