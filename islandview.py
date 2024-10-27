import signal
import time
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

def get_pixel_color(x, y):
    '''Get the color of the pixel at (x, y)'''
    screenshot = ImageGrab.grab()
    return screenshot.getpixel((x, y))

def color_match(color1, color2, tolerance=20):
    '''Check if two colors match within a given tolerance'''
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def search_color(target_color, npcteller, rois=None, tolerance=20, wait=0.1):
    '''Search for a target color within specified regions of interest (ROIs)'''
    rois = rois or []
    status, found_x, found_y = 0, None, None

    for roi in rois:
        x1, y1, width, height, name = roi
        for x in range(x1, x1 + width, 10):
            for y in range(y1, y1 + height, 10):
                current_color = get_pixel_color(x, y)
                if color_match(current_color, target_color, tolerance):
                    pyautogui.moveTo(x, y)
                    time.sleep(wait)
                    pyautogui.click(button='left')
                    status += 1
                    print(npcteller, name, "found color at", x, y)
                    npcteller += 1
                    found_x, found_y = x, y
                    return npcteller, status, found_x, found_y

    return npcteller, status, found_x, found_y

def main():
    '''Main function'''
    enable_ctrl_c()
    loop_counter, npc_counter = 0, 1
    target_color_list = [
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

    for target_color, description in target_color_list:
        print(f"Searching for {description}")
        npc_counter, status, found_x, found_y = search_color(target_color, npc_counter, rois=SMURFWINDOWS, tolerance=20)
        if status > 0:
            print(f"Found {description} at {found_x}, {found_y}")
        else:
            print(f"{description} not found")

    print("====Ready")
    pyautogui.moveTo(2759, 44)
    time.sleep(0.5)
    pyautogui.click(button='left')

if __name__ == '__main__':
    main()
