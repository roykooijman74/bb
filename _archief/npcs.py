import signal
import time
from functools import partial
import threading
import pyautogui
from PIL import ImageGrab

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

SMURFWINDOWS = [
    [2560, 0, 790, 460, 'Smurf 1'],
    [3414, 0, 790, 460, 'Smurf 2'],
    [4267, 0, 790, 460, 'Smurf 3'],
    [2560, 461, 790, 460, 'Smurf 4'],
    [3414, 461, 790, 460, 'Smurf 5'],
    [4267, 461, 790, 460, 'Smurf 6'],
    # [2560, 921, 790, 460, 'Smurf 7'],
    # [3414, 921, 790, 460, 'Smurf 8'],
    # [4267, 921, 790, 460, 'Smurf 9'],
    # [1770, 0, 790, 460, 'Smurf 0'],
    # [1770, 461, 790, 460, 'A Supersmurf'],
    # [1770, 921, 790, 460, 'B MiniSmurf']

]

# Define constants for image paths
IMAGES = {
    'invasie': "images/npc-invasie2.png",
    'beloning': "images/beloningophalen.png",
    'promoted': "images/promoted.png",
    'chest_open': "images/chest.png",
    'claimen': "images/claimen.png"
}

def enable_ctrl_c():
    '''Enable Ctrl-C interruption'''
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def handle_drt():
    "function to handle if Dr t is in screen coordinates"
    

def open_menu_list(x1, y1):
    '''Function to open the menu list'''
    # Implement the logic to open the menu list

def close_menu_list(x1, y1):
    '''Function to close the menu list'''
    # Implement the logic to close the menu list

def handle_invasie(smurf_info):
    '''Function to handle invasie'''
    # Implement the invasie handling logic

def handle_beloning(smurf_info):
    '''Function to handle beloning'''
    # Implement the beloning handling logic

def handle_promoted(smurf_info):
    '''Function to handle promoted'''
    # Implement the promoted handling logic

def handle_chest(smurf_info):
    '''Function to handle chest opening and claiming'''
    x1, y1, width, length, name = smurf_info
    if pyautogui.locateOnScreen(IMAGES['claimen'], confidence=0.7, region=(x1, y1, width, length)):
        pyautogui.click(x1 + rel_x, y1 + rel_y)
        pyautogui.click(pos1, pos2)



def search_image(image_path, smurf_info, offset=0, confidencevalue=0.7, wait=0.1):
    '''Search for an image within a specified region of interest (ROI)'''
    x1, y1, width, length, name = smurf_info
    print("searching image", image_path, "for", name)
    location = pyautogui.locateCenterOnScreen(image_path, confidence=confidencevalue, region=(x1, y1, width, length))
    if location:
        x, y = location[0], location[1] + offset
        pyautogui.moveTo(x, y)
        time.sleep(wait)
        pyautogui.click(button='left')
        return x, y, name
    return None, None, name

def drag_menu_down(smurf):
    '''Function to drag menu down based on loop counter'''
    x, y, width, length, name = smurf
    x_up=100
    y_up=75
    x_down=100
    y_down=430
    clickdown_pos_x=x+x_down
    clickdown_pos_y=y+y_down
    clickup_pos_x=x+x_up
    clickup_pos_y=y+y_up
    pyautogui.moveTo(clickdown_pos_x, clickdown_pos_y)
    time.sleep(0.2)
    pyautogui.click(button='left')
    pyautogui.dragTo(clickup_pos_x, clickup_pos_y)

def open_menu(smurf):
    x, y, width, length, name = smurf
    x_relative=20
    y_relative=100
    clickpos_x=x+x_relative
    clickpos_y=y+y_relative
    pyautogui.moveTo(clickpos_x, clickpos_y)
    time.sleep(0.2)
    pyautogui.click(button='left')


def close_menu(smurf):
    x, y, width, length, name = smurf
    x_relative=200
    y_relative=50
    clickpos_x=x+x_relative
    clickpos_y=y+y_relative
    pyautogui.moveTo(clickpos_x, clickpos_y)
    time.sleep(0.2)
    pyautogui.click(button='left')


def handle_smurf(smurf_info, activity_log_page):
    #handle_diamond(smurf_info)
    open_menu(smurf_info)
    current_activity_page = 0
    if current_activity_page < activity_log_page:
        drag_menu_down(smurf_info)
  
    for y_offset in range(80, 440, 30):
#        click_on_activity(smurf_info, y_offset)
#        handle_drt(smurf_info)
#        handle_promoted(smurf_info)
#        handle_chest(smurf_info)
#        handle_reward(smurf_info)
        x,y,name= search_image(IMAGES['invasie'], smurf_info, offset=70, wait=0.1)
        if x!=None and y!=None and name!=None:
            print(x,y,name)

    close_menu(smurf_info)
    time.sleep(1)

def main():
    enable_ctrl_c()

    #the max activity log is 6 pages
    activity_log_pages = 6
    for activity_log_page in range(activity_log_pages):
        for smurf in SMURFWINDOWS:
            handle_smurf(smurf, activity_log_page)

if __name__ == '__main__':
    main()
