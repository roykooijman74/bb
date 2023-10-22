import pyautogui
import time
import signal

from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

def enablectrlc():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def zoekimage(image, text, counters):
    try: 
        image_location = pyautogui.locateCenterOnScreen(image, confidence=0.7)
        if image_location:
            counters[text] += 1
            x, y = image_location
            xpos, ypos = pyautogui.position()
            pyautogui.moveTo(x=x-1920, y=y)
            pyautogui.click(button='left')
            pyautogui.moveTo(xpos, ypos)
            print(f"{image} found at {x}, {y}. Count: {counters[text]}")
        else:
            print(f"{image} not found")
    except Exception as e:
        print(f"Error: {e}")

def main():
    counters = {
        "maken1": 0,
        "maken2": 0,
        "maken3": 0,
        "actie": 0,
        "inzetten1": 0,
        "inzetten2": 0,
        "inzetten3": 0,
        "7scherven": 0,
        "recycle-bruin": 0,
        "recycle-groen": 0
    }
    enablectrlc()
    pyautogui.moveTo(960, 540)
    while True:
        zoekimage("images/beeldhouwermaken.png", "maken1", counters)
        zoekimage("images/beeldhouwermaken2.png", "maken2", counters)
        zoekimage("images/beeldhouwermaken3.png", "maken3", counters)
        zoekimage("images/beeldhouwerbeeldactie.png", "actie", counters)
        zoekimage("images/beeldinzetten.png", "inzetten1", counters)
        zoekimage("images/beeldinzetten2.png", "inzetten2", counters)
        zoekimage("images/beeldinzetten3.png", "inzetten3", counters)
        zoekimage("images/beeldhouwer7scherven.png", "7scherven", counters)
        zoekimage("images/beeldhouwer-recycle-bruin.png", "recycle-bruin", counters)
        zoekimage("images/beeldhouwer-recycle-groen.png", "recycle-groen", counters)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
