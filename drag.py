import sys
import pyautogui


def drag_window(direction):
    '''Drag the window in the specified direction.'''
    start_x, start_y, end_x, end_y = 0, 0, 0, 0

    if direction == "up":
        start_x, start_y, end_x, end_y = 2880, 100, 2880, 385
        duration = 0.4
    elif direction == "down":
        start_x, start_y, end_x, end_y = 2880, 385, 2880, 100
        duration = 0.4
    elif direction == "left":
        start_x, start_y, end_x, end_y = 3200, 222, 2800, 222
        duration = 0.7
    elif direction == "right":
        start_x, start_y, end_x, end_y = 2800, 222, 3200, 222
        duration = 0.7

    print(f"Dragging {direction}")
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=duration)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=0.1)
    pyautogui.mouseUp()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python drag.py [left|right|up|down]")
    else:
        direction = sys.argv[1]
        if direction in ["left", "right", "up", "down"]:
            drag_window(direction)
        else:
            print("Invalid direction. Use 'left', 'right', 'up', or 'down'.")
