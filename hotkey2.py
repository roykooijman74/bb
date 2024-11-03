import win32api
import win32con
import time

# Define the hotkey as the Tab key
CTRL_KEY = win32con.VK_CONTROL  # Define the control key

def main():
    count = 0
    while True:
        # Check if Ctrl key is pressed down, if so, exit the loop
        if win32api.GetAsyncKeyState(CTRL_KEY) & 0x8000:
            print("Ctrl key pressed. Exiting...")
            break
        
        # Increment the count, print, and wait
        count += 1
        print(f"Count: {count}")
        time.sleep(0.5)

if __name__ == '__main__':
    main()
