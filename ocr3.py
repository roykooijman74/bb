import pyautogui
import time
import signal
import re
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

import pytesseract                  #ocr
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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


#3223 61 3290 73 67 12 [2560, 0, 790, 460, 'Smurf 1']
#4077 61 4144 73 67 12 [3414, 0, 790, 460, 'Smurf 2']
#4930 61 4997 73 67 12 [4267, 0, 790, 460, 'Smurf 3']
#3223 522 3290 534 67 12 [2560, 461, 790, 460, 'Smurf 4']
#4077 522 4144 534 67 12 [3414, 461, 790, 460, 'Smurf 5']
#4930 522 4997 534 67 12 [4267, 461, 790, 460, 'Smurf 6']
#3223 982 3290 994 67 12 [2560, 921, 790, 460, 'Smurf 7']
#4077 982 4144 994 67 12 [3414, 921, 790, 460, 'Smurf 8']
#4930 982 4997 994 67 12 [4267, 921, 790, 460, 'Smurf 9']
#2433 61 2500 73 67 12 [1770, 0, 790, 460, 'Smurf 0']
#2433 522 2500 534 67 12 [1770, 461, 790, 460, 'A Supersmurf']
#2433 982 2500 994 67 12 [1770, 921, 790, 460, 'B MiniSmurf']

#Page segmentation modes:
#  0    Orientation and script detection (OSD) only.
#  1    Automatic page segmentation with OSD.
#  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
#  3    Fully automatic page segmentation, but no OSD. (Default)
#  4    Assume a single column of text of variable sizes.
#  5    Assume a single uniform block of vertically aligned text.
#  6    Assume a single uniform block of text.
#  7    Treat the image as a single text line.
#  8    Treat the image as a single word.
#  9    Treat the image as a single word in a circle.
# 10    Treat the image as a single character.
# 11    Sparse text. Find as much text as possible in no particular order.
# 12    Sparse text with OSD.
# 13    Raw line. Treat the image as a single text line,
#       bypassing hacks that are Tesseract-specific.
#
#OCR Engine modes:
#  0    Legacy engine only.
#  1    Neural nets LSTM engine only.
#  2    Legacy + LSTM engines.
#  3    Default, based on what is available.



#cropped_image.show()
text = ""
loop=0

while text=="":
    screenshot = pyautogui.screenshot()
    screenshot_gray = screenshot.convert('L')
    #region = (3247, 61, 3290,73)
    region=(4077, 982, 4140, 994) #smurf 8
    cropped_image = screenshot_gray.crop(region)
    loop=loop+1
    #text = pytesseract.image_to_string(cropped_image)
    custom_config = r'--oem 3    --psm 7'
    text = pytesseract.image_to_string(cropped_image, config=custom_config)
    numeric_value = int(re.sub(r'\D', '', text))
    print(loop,text, numeric_value, custom_config)
#print(text)


#regions = {}  # Create a dictionary to store regions for each Smurf

#for smurf in SMURFWINDOWS:
#    x, y, width, height, name = smurf
#    region = (x, y, x + width, y + height)
#    regions[name] = region
    
# Print regions for all Smurfs
#for smurf_name, region_coords in regions.items():
#    print(f"Region for {smurf_name}: {region_coords}")
    
    