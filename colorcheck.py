from functools import partial
import pyautogui
from PIL import ImageGrab

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

#itempositions and colors   x,y,r,g,b
attackmenu = [22, 108, 243, 243, 241]
claimen_text  = [98, 375, 167, 218, 65]
selecterenscherf = [226, 371, 168, 224, 80]

def check_color_at_x_y(item):
    #get the current pixel color
    pixel_color = pyautogui.pixel(item[0], item[1])
    #print(pixel_color)
    r_get=pixel_color[0]
    g_get=pixel_color[1]
    b_get=pixel_color[2]

    if r_get == item[2] and g_get == item[3] and b_get == item[4]:
        return True
    else:
        return False

print("yes" if check_color_at_x_y(claimen_text) else "no")

    

