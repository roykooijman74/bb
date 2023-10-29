import win32api
import win32con

# Define the hotkey as the Tab key
HOTKEY = win32con.VK_TAB

# Flag to track if the hotkey has been pressed
hotkey_pressed = False


def check_hotkey():
    global hotkey_pressed
    while not hotkey_pressed:
        if win32api.GetAsyncKeyState(HOTKEY) & 0x8000:
            hotkey_pressed = True


def main():
    print("Waiting for the Tab key to be pressed...")
    check_hotkey()
    print("Tab key pressed. Continuing with the script.")


if __name__ == '__main__':
    main()
