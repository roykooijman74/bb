'''#print window titles

import win32gui

def get_window_titles():
    titles = []
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            titles.append(win32gui.GetWindowText(hwnd))
        return True
    win32gui.EnumWindows(callback, None)
    return titles

# Get a list of all visible window titles
window_titles = get_window_titles()

# Sort the window titles in lexicographically order
window_titles.sort()

# Print the window titles
for title in window_titles:
    print(title)
'''

import win32gui

def get_window_coords():
    coords = []
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            width = rect[2] - x
            height = rect[3] - y
            title = win32gui.GetWindowText(hwnd)
            coords.append((title, x, y, width, height))
        return True
    win32gui.EnumWindows(callback, None)
    return coords

# Get a list of all visible window titles and their coordinates
window_coords = get_window_coords()

# Sort the window titles in lexicographically order
window_coords.sort()

# Print the window titles and their coordinates
for title, x, y, width, height in window_coords:
    print(f"{title}: ({x}, {y}), {width} x {height}")
