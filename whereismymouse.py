"""Python3.11"""


import pyautogui


def main():
    '''main function'''
    # Get the current position of the mouse cursor
    x, y = pyautogui.position()

    # Print the cursor position
#    print('X: {}, Y: {}'.format(x, y))
    #print(f'X: {x}, Y: {y}')

    # Get the color of the pixel at the given coordinates
    pixel_color = pyautogui.pixel(x, y)  # type: ignore

    # Print the RGB values of the pixel color
    print(f'"thing": [{x}, {y}, {pixel_color[0]}, {pixel_color[1]}, {pixel_color[2]}]')
    print(f'item = [{x}, {y}, {pixel_color[0]}, {pixel_color[1]}, {pixel_color[2]}]')

    print(f'smurf 1 item = [{x-2560}, {y}, {pixel_color[0]}, {pixel_color[1]}, {pixel_color[2]}, "item"]')
    print(f'smurf 2 item = [{x-3414}, {y}, {pixel_color[0]}, {pixel_color[1]}, {pixel_color[2]}, "item"]')
    print(f'smurf 3 item = [{x-4267}, {y}, {pixel_color[0]}, {pixel_color[1]}, {pixel_color[2]}, "item"]')


    #print(type(pixel_color))

if __name__ == '__main__':
    main()
