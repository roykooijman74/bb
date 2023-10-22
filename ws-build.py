import pyautogui
import time
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import signal



def enablectrlc():
    # KeyboardInterrupt: Ctrl-C
    # dependent on import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def zoek_offset(plaatje,offsetx,i):
    try:
        imagex,imagey = pyautogui.locateCenterOnScreen(plaatje, confidence=0.8)     
    except:
        status=False
        imagex=0
        imagey=0
    else:
        xpositie,ypositie=pyautogui.position()
        status=True
        pyautogui.moveTo(x=imagex-2560+offsetx,y=imagey)#Moves the mouse to the coordinates of the image, let op 1920 eraf omdat monitors anders uitkomen///
        time.sleep(0.1)
        pyautogui.click(button='left')
        pyautogui.moveTo(xpositie,ypositie)
    finally:
        print(i,status,imagex,imagey,plaatje)
        return status,imagex,imagey

def main():
    enablectrlc()
    i=0
    while True:
        i=i+1
        zoek_offset("images\ws-place-ok.png",0,i)
        time.sleep(0.1)
        if i==5:
            pyautogui.moveTo(74,409)
            pyautogui.click(button='left') 
            i=0
    
     
if __name__ == '__main__':
    main()
