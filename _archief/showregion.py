import pyautogui
from PIL import Image
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


SMURFWINDOWS=[
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

def capture_and_display_region(x, y, width, height):
    # Capture the screen region
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Display the captured image
    screenshot.show()

def main():
    x = 2560  # X-coordinate of the top-left corner of the region
    y = 0  # Y-coordinate of the top-left corner of the region
    width = 790  # Width of the region
    height = 460  # Height of the region

    capture_and_display_region(x, y, width, height)

if __name__ == '__main__':
    main()
