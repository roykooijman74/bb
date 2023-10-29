''' python 3.11 '''
import win32api
import win32con

# Define the hotkey as the Tab key
HOTKEY = win32con.VK_TAB

# Flag to track if the hotkey has been pressed


def check_hotkey():
    '''Check if	hotkey is pressed.'''
    hotkey_pressed = False
    while not hotkey_pressed:
        if win32api.GetAsyncKeyState(HOTKEY) & 0x8000:  # pylint: disable=I1101
            hotkey_pressed = True


def main():
    '''main function.'''
    print("Waiting for the Tab key to be pressed...")
    check_hotkey()
    print("Tab key pressed. Continuing with the script.")


if __name__ == '__main__':
    main()
