import signal
import time
from functools import partial
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
    [2560, 921, 790, 460, 'Smurf 7'],
    [3414, 921, 790, 460, 'Smurf 8'],
    [4267, 921, 790, 460, 'Smurf 9'],
    [1770, 0, 790, 460, 'Smurf 0'],
    [1770, 461, 790, 460, 'A Supersmurf'],
    [1770, 921, 790, 460, 'B MiniSmurf']

]

ITEM_POSITION = [{"reward_chest": [13, 372, 94, 389]},
                {"defense_diamonds": [146,60,190,451]}
                ]

#itempositions and colors   x,y,r,g,b
attackmenu = [22, 108, 243, 243, 241]
claimen_text  = [98, 375, 167, 218, 65]



def check_rgb_at_coordinates(item):
    # Extract the expected values from claimen_text
    x = item[0]
    y = item[1]
    r = item[2]
    g = item[3]
    b = item[4]
    
    #get the current pixel color
    pixel_color = pyautogui.pixel(item[0], item[1])  
    r_get=pixel_color[0]    
    g_get=pixel_color[1]    
    b_get=pixel_color[2]    

    if r_get and item[2] and g_get and item[3] and b_get and item[4]:
        return True
    else:
        return False

print(check_rgb_at_coordinates(claimen_text)
    

    
    
# kistposrel
# X: 13, Y: 372, Xend: 94, Yend: 389
# defencediam
# X: 146, Y: 60, Xend: 199, Yend: 451

#gedegradeerd   X: 231, Y: 72    RGB values: (0, 0, 0)

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

    # #!gedegradeerd   X: 231, Y: 72    RGB values: (0, 0, 0)

    # for smurf_info in SMURFWINDOWS:
    #     x1, y1, width, length, name = smurf_info
    #     checkx=x1+231
    #     checky=y1+72
    #     # Get the color of the pixel at the given coordinates
    #     pixel_color = pyautogui.pixel(checkx, checky)  # type: ignore
    #     # Print the RGB values of the pixel color
    #     print(f"RGB values: {pixel_color}")
    #     if pixel_color[0]==0:
    #         print("black", name,pixel_color[0])
    #     else:
    #         print("NOT black", name, pixel_color[0])

    #! vernietigen

    for smurf_info in SMURFWINDOWS:
        x, y, found_name = search_image(IMAGES['invasie'], smurf_info, offset=70, wait=0.1)
        if x:
            time.sleep(2.0)

            x1, y1, width, length, name = smurf_info
            delta_x = x - x1
            delta_y = y - y1
            print(name, "x:", delta_x, "y:", delta_y)
            if 470 <= delta_x <= 490 and 280 <= delta_y <= 310:
                print(name, "function click middle")
                colorposx=x1+478
                colorposy=y1+190
                pixel_color = pyautogui.pixel(colorposx, colorposy)
                print(pixel_color, "compare with RGB values: (187, 156, 75))")
                
                # X: 478, Y: 190
                # RGB values: (187, 156, 75)
                
            elif 340 <= delta_x <= 370 and 275 <= delta_y <= 310:
                colorposx=x1+352
                colorposy=y1+192
                pixel_color = pyautogui.pixel(colorposx, colorposy)
                print(pixel_color, "compare with RGB values: (187, 157, 75)")
                print(name, "function click left")
                # X: 352, Y: 192
                # RGB values: (187, 157, 75)
        else:
            print(name, "image not found")




# searching image images/npc-invasie2.png for Smurf 1
# Smurf 1  x: 354 y 307
# searching image images/npc-invasie2.png for Smurf 2
# Smurf 2 image not found
# searching image images/npc-invasie2.png for Smurf 3
# Smurf 3  x: 480 y 288
# searching image images/npc-invasie2.png for Smurf 4
# Smurf 4  x: 480 y 308
# searching image images/npc-invasie2.png for Smurf 5
# Smurf 5  x: 479 y 302

    # #the max activity log is 6 pages
    # activity_log_pages = 6
    # for activity_log_page in range(activity_log_pages):
    #     for smurf in SMURFWINDOWS:
    #         handle_smurf(smurf, activity_log_page)

if __name__ == '__main__':
    main()
