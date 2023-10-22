import pyautogui
import time
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import signal
import pyttsx3

def enablectrlc():
    # KeyboardInterrupt: Ctrl-C
    # dependent on import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def zoekplaatje(plaatje,offset=0,confidencevalue=0.9):
    xpositie,ypositie=pyautogui.position()
    try:
        imagex,imagey = pyautogui.locateCenterOnScreen(plaatje, confidence=confidencevalue)
    except:
        status=False
        imagex=0
        imagey=0
    else:
        status=True
        x=imagex#-2560
        y=imagey+offset
        pyautogui.moveTo(x,y)
        pyautogui.click(button='left')
        print("found",plaatje)
    finally:
        return status,imagex,imagey


def main():
    enablectrlc()
    while True:
        print("searching android start")
        zoekplaatje("images/start-android.png")
        print("searching boombeach app start")
        zoekplaatje("images/start-boombeach.png")
        time.sleep(0.5)
        
if __name__ == '__main__':
    main()
