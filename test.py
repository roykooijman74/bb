'''python 3.11'''
import win32gui
hwnd = win32gui.FindWindow(None, "win32")  # pylint: disable=I1101
print(hwnd)
