"""Python3.11"""


import pyautogui


def main():
    '''main function'''
    # Get the current position of the mouse cursor
    x, y = pyautogui.position()

    # Print the cursor position
#    print('X: {}, Y: {}'.format(x, y))
    print(f'X: {x}, Y: {y}')

    # Get the color of the pixel at the given coordinates
    pixel_color = pyautogui.pixel(x, y)  # type: ignore

    # Print the RGB values of the pixel color
    print(f"RGB values: {pixel_color}")


if __name__ == '__main__':
    main()
