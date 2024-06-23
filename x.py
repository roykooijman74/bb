import time
from functools import partial
import pyautogui
#vars
from variables import * # yes import all the variables
from functions import enable_ctrl_c
from functions import WindowsChecker as WC

from PIL import ImageGrab
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


def search_image(image_path,window, confidencevalue=0.7):
    x1, y1, width, length, name = window
    location = pyautogui.locateCenterOnScreen(image_path, confidence=confidencevalue, region=(x1, y1, width, length))
    if location:
        x, y = location[0], location[1]
    return x,y

def item_real_position_on_screen(item,window):
    x, y, _, _,_ = window
    rel_x=item[0]
    rel_y=item[1]
    #print(x,y,x+rel_x,y+rel_y)
    return(x+rel_x,y+rel_y)


def open_attack_menu(windows, item=None):
    #open attackmenu if not opened
    if item==None: item=open_attack_menu_item
    for window in windows:
        item_real_x,item_real_y= item_real_position_on_screen(item,window)
        check=WC.check_color_at_x_y(item_real_x,item_real_y,item[2],item[3],item[4])
        print(window[4],item[5],check,item[2],item[3],item[4])
        if check:
            pyautogui.leftClick(item_real_x, item_real_y)

def close_attack_menu(windows, item=None):
    # item=close_attack_menu_item
    if item==None: item=close_attack_menu_item
    for window in windows:
        item_real_x,item_real_y= item_real_position_on_screen(item,window)
        check=False
        while check==False:
            check=WC.check_color_at_x_y(item_real_x,item_real_y,item[2],item[3],item[4])
            print(window[4],item[5],check,item[2],item[3],item[4])
            if check:
                pyautogui.leftClick(item_real_x, item_real_y)
            time.sleep(0.2)


def check_item(windows, item=None):
    #open attackmenu if not opened
    if item==None: exit()
    for window in windows:
        item_real_x,item_real_y= item_real_position_on_screen(item,window)
        check=WC.check_color_at_x_y(item_real_x,item_real_y,item[2],item[3],item[4])
        print(window[4],item[5],check,item[2],item[3],item[4])
        if check:
            pyautogui.leftClick(item_real_x, item_real_y)

# def check_item2(window = None, item=None):
#     #open attackmenu if not opened
#     item_real_x,item_real_y= item_real_position_on_screen(item,window)
#     check=WC.check_color_at_x_y(item_real_x,item_real_y,item[2],item[3],item[4])
#     print(window[4],item[5],check,item[2],item[3],item[4])
#     if check:
#         pyautogui.leftClick(item_real_x, item_real_y)


    




def main():
    enable_ctrl_c()

    print("="*40," ","check active windows")
    windows = WC.check_active_windows(smurfwindows)
    print("="*40," ","sync stop button")
    print(smurfwindows[0])

    print("="*40," ","check if sync button is active windows")
    check_item2(smurfwindows[0],sync_stop_button)
    
    

    print("="*40," ","close chat menu")
    for window in windows: check_item2(window,close_chat_menu)
    for window in windows: check_item2(window,open_attack_menu_item)
    #for window in windows: check_item2(window=window,item=close_attack_menu_item)

    #open_attack_menu()
    close_attack_menu(windows)

    #check claimen
    for smurf in windows:
        item=claimen_text
        item_real_x,item_real_y= item_real_position_on_screen(item,smurf)
        check=WC.check_color_at_x_y(item_real_x,item_real_y,item[2],item[3],item[4])
        print(smurf[4],item[5],check,item[2],item[3],item[4])
        if check:
            print("click on claimen")
            pyautogui.leftClick(item_real_x, item_real_y)

#            time.sleep(0.3)

            item=select_sharf
            item_real_x,item_real_y= item_real_position_on_screen(item,smurf)
            check2=False
            while check2==False:
                check2=WC.check_color_at_x_y(item_real_x,item_real_y,item[2],item[3],item[4])
                time.sleep(0.1)
            if check2:
                pyautogui.moveTo(item_real_x, item_real_y)

            #pyautogui.leftClick(item_real_x, item_real_y)

            #time.sleep(0.2)
            #pyautogui.click(button='left')



if __name__ == '__main__':
    main()
