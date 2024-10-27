import signal
import time
import pyautogui
from PIL import ImageGrab
from functools import partial

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

TARGET_COLOR_LIST = [
    (252, 190, 0, "Invasie midden"),
    (211, 157, 6, "INVASIE LEFT SMURF 5"),
    (160, 220, 72, "Reward mini with 4 and ss"),
    (96, 184, 228, "TROOP DEATH REVIVE"),
    (255, 215, 0, "OKAY MONEY ON REVIVAL"),
    (200, 168, 80, "VERNIETIGEN NPC BROWN"),
    (160, 216, 72, "Vernietigen groen"),
    (38, 61, 75, "WHEN DRT SAYS STUFF THE BLUE LEVEL ROUND THING IS DARK BLUE"),
    (63, 53, 40, "DRT STUPID SUNGLASS"),
    (228, 217, 192, "STUPID GUY AFTER DRT TALK 2x"),
    (54, 129, 170, "NORMAL WINDOW"),
]

class WindowsChecker:
    @staticmethod
    def enable_ctrl_c():
        '''Enable Ctrl-C interruption'''
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    @staticmethod
    def get_pixel_color(x, y):
        '''Get the color of the pixel at (x, y)'''
        screenshot = ImageGrab.grab()
        return screenshot.getpixel((x, y))

    @staticmethod
    def color_match(color1, color2, tolerance=20):
        '''Check if two colors match within a given tolerance'''
        return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

    @staticmethod
    def check_color_at_x_y(description, rois=None, tolerance=20):
        '''Check if a color matching the given description is found in the specified ROIs'''
        target_color = next((color for color, desc in TARGET_COLOR_LIST if desc == description), None)
        if not target_color:
            print(f"Description '{description}' not found in the target color list.")
            return False

        rois = rois or SMURFWINDOWS
        for roi in rois:
            x1, y1, width, height, name = roi
            for x in range(x1, x1 + width, 10):
                for y in range(y1, y1 + height, 10):
                    current_color = WindowsChecker.get_pixel_color(x, y)
                    if WindowsChecker.color_match(current_color, target_color, tolerance):
                        print(f"{description} color found at {x}, {y} in {name}.")
                        return True
        print(f"{description} color not found.")
        return False

def main():
    '''Main function'''
    WindowsChecker.enable_ctrl_c()

    # Example usage:
    status = WindowsChecker.check_color_at_x_y("NORMAL WINDOW")
    if status:
        print("Color match found.")
    else:
        print("Color match not found.")

if __name__ == '__main__':
    main()
