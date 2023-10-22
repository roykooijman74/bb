import pyautogui
import time
import signal
from PIL import ImageGrab
from functools import partial
import pytesseract                  #ocr
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

#X: 3244, Y: 63              X: 3290, Y: 72


def enablectrlc():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def zoekplaatje(image_path, offset=0, confidencevalue=0.7, rois=None, wait=0.0):
    status = 0
    print("start search")
    while True:  # Loop until no instances are found in any ROI
        found = False  # Flag to check if any instance was found in this iteration
        screenshot = pyautogui.screenshot()
        for roi in rois:
            x1, y1, width, length, name = roi
            location = None
            try:
                # Capture a screenshot of the entire screen

                # Define the region to capture (left, top, width, height)
                #region = (x1+3224-2560, y1+63, 3290-3244, 72-63)
                region=(3224, 63, 56,9)
                print(name, region)
                # Crop the screenshot to the defined region
                cropped_image = screenshot.crop(region)

                # Perform OCR on the cropped image
                text = pytesseract.image_to_string(cropped_image)

                # Print the extracted text
                print(text)
            
                
                #location = pyautogui.locateCenterOnScreen(image_path, confidence=confidencevalue, region=(x2, y2, width2, length2))
            except:
                pass

            if location:
                #x = location[0]
                #y = location[1] + offset
                #pyautogui.moveTo(x, y)
                #time.sleep(wait)
                #pyautogui.click(button='left')
                #status += 1
                #found = True
                print("=============================", x, y, status, image_path, name)
        if not found:
            break  # If no instances were found in this iteration, exit the loop
    return status


def main():
    enablectrlc()
    zoekplaatje("images\kistje.png", 0, rois=SMURFWINDOWS)

if __name__ == '__main__':
    false_counter = 0
    main()


