"""Python3.11"""
import win32gui


def get_window_coords():
    '''Returns the coordinates	'''
    coords = []

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            titel = win32gui.GetWindowText(hwnd)
            coords.append((titel, x, y, w, h))
        return True
    win32gui.EnumWindows(callback, None)
    return coords


# Get a list of all visible window titles and their coordinates
window_coords = get_window_coords()

# Sort the window titles in lexicographically order
window_coords.sort()

# Print the window titles and their coordinates
for title, x_window, y_window, width, height in window_coords:  # Changed variable names
    print(f"{title}: ({x_window}, {y_window}), {width} x {height}")
