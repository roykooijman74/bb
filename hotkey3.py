import win32api
import win32con
import time
import threading
import os

# Define the control key
CTRL_KEY = win32con.VK_CONTROL

def countdown(duration):
    for i in range(duration, 0, -1):
        print(f"Countdown: {i}         ", end='\r')
        time.sleep(1)
    print("Countdown: 0")

def check_ctrl_key():
    """Thread function to check for Ctrl key press."""
    while True:
        # Check if Ctrl key is pressed down; if so, exit the program immediately
        if win32api.GetAsyncKeyState(CTRL_KEY) & 0x8000:
            print("Ctrl key pressed. Exiting program immediately...")
            os._exit(0)  # Immediately terminate the program

def main():
    """Main counting function."""
    count = 0
    while True:
        # Increment the count, print, and wait
        count += 1
        print(f"Count: {count}")
        countdown(3)

if __name__ == '__main__':
    # Start the Ctrl key check thread
    ctrl_thread = threading.Thread(target=check_ctrl_key)
    ctrl_thread.daemon = True  # Set as a daemon so it won't prevent program exit
    ctrl_thread.start()

    # Run the main counting function
    main()
