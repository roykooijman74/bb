import pytesseract  # ocr
import pyautogui
import time
import signal
import re

from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

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


def gettext(region):
    text = ""
    loop = 0

    while text == "":
        screenshot = pyautogui.screenshot()
        screenshot_gray = screenshot.convert('L')
        cropped_image = screenshot_gray.crop(region)
        loop = loop+1
        # text = pytesseract.image_to_string(cropped_image)
        custom_config = r'--oem 3    --psm 7'
        text = pytesseract.image_to_string(cropped_image, config=custom_config)
        print(text)
        screenshot = ()
    numeric_value = int(re.sub(r'\D', '', text))
    print(loop, numeric_value)
    return numeric_value


smurf1_corrected_coords = SMURFWINDOWS[0][0:4]
smurf1_corrected_region = [3247, 57, 3290, 77]  # 3223 61 67 12

x, y = smurf1_corrected_coords[0:2]
x2, y2, x2end, y2end = smurf1_corrected_region[0:4]
x_delta = x2-x
y_delta = y2-y
x_width = x2end-x2
y_width = y2end-y2
x2end_delta = x2-x+x_delta
y2end_delta = y2-y+y_delta

for roi in SMURFWINDOWS[:]:
    xx = roi[0]+x_delta
    yy = roi[1]+y_delta
    xxend = xx+x_width
    yyend = yy+y_width
    # print(roi[4],[xx,yy,xxend,yyend])
    # print(xx,yy,xxend,yyend,x_width,y_width, roi)
    gettext([xx, yy, xxend, yyend])
    # print(diams)
