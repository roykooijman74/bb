import win32gui

#BlueStacks Multi Instance Manager: (1084, 707), 692 x 687

hwnd = win32gui.FindWindow(None, "BlueStacks Multi Instance Manager")

if hwnd:
     # get current window position and size
     _, _, win_width, win_height = win32gui.GetWindowRect(hwnd)
     # set new window position and size
     win_pos_x, win_pos_y, win_width_new, win_height_new = [1084, 707, 700, 687]
     # move window
     win32gui.SetWindowPos(hwnd, None, win_pos_x, win_pos_y, win_width_new, win_height_new, 0x0001)
     # resize window
     win32gui.SetWindowPos(hwnd, None, win_pos_x, win_pos_y, win_width_new, win_height_new, 0x0002 | 0x0040)
else:
        print(f"Window '{window[4]}' not found.")
