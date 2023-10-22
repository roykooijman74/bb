import pyautogui

# Get the current position of the mouse cursor
x, y = pyautogui.position()

# Print the cursor position
print('X: {}, Y: {}'.format(x, y))


# Get the color of the pixel at the given coordinates
pixel_color = pyautogui.pixel(x, y)

# Print the RGB values of the pixel color
print(f"RGB values: {pixel_color}")