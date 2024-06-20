''' helper functions for smurf project'''
import signal
from functools import partial
import win32gui
import pyautogui
from PIL import ImageGrab
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


def enable_ctrl_c():
    """Enable Ctrl-C interruption"""
    signal.signal(signal.SIGINT, signal.SIG_DFL)


class WindowsChecker:
    ''' defines all the windows related functions'''

    @staticmethod
    def check_active_windows(windows):
        ''' there are 12 smurfs but not all have to be active so this returns only the active windows'''
        active = []
        for window in windows:
            print("zoeken naar: ", window[4])
            hwnd = win32gui.FindWindow(None, window[4])
            if hwnd:
                active.append(window)
        print("active windows = ", active)
        return active

    @staticmethod
    def check_color_at_x_y(x, y, r, g, b, variance=5):
        '''in the game a color on a position is checked against what is expected'''
        # Get the current pixel color
        pixel_color = pyautogui.pixel(x, y)
        # Extract RGB values
        r_get = pixel_color[0]
        g_get = pixel_color[1]
        b_get = pixel_color[2]
        # Check if each color is within the variance of the value searched for
        if (
            (r - variance <= r_get <= r + variance)
            and (g - variance <= g_get <= g + variance)
            and (b - variance <= b_get <= b + variance)
        ):
            return True
        else:
            return False
