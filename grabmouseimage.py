import os
import argparse
from functools import partial
import pyautogui
from PIL import ImageGrab

# Configure ImageGrab to grab from all screens
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

# List of all windows (Smurfs) with coordinates and names
all_smurf_windows = [
    [2560, 0, 790, 460, 'Smurf 1'],
    [3414, 0, 790, 460, 'Smurf 2'],
    [4267, 0, 790, 460, 'Smurf 3'],
    [2560, 461, 790, 460, 'Smurf 4'],
    [3414, 461, 790, 460, 'Smurf 5'],
    [4267, 461, 790, 460, 'Smurf 6'],
    [2560, 921, 790, 460, 'Smurf 7'],
    [3414, 921, 790, 460, 'Smurf 8'],
    [4267, 921, 790, 460, 'Smurf 9'],
    [1770, 0, 790, 460, 'A Supersmurf'],
    [1770, 461, 790, 460, 'B MiniSmurf'],
    [1770, 921, 790, 460, 'C KickSmurf'],
]

def find_window_by_position(x, y):
    for window in all_smurf_windows:
        win_x, win_y, width, height, name = window
        if win_x <= x < win_x + width and win_y <= y < win_y + height:
            return window
    return None

def capture_region(length, height, imagename):
    # Get the current mouse position
    x, y = pyautogui.position()
    print(f"Mouse position: x={x}, y={y}")

    # Identify the window containing the mouse position
    window = find_window_by_position(x, y)
    if window:
        win_x, win_y, _, _, win_name = window
        rel_x, rel_y = x - win_x, y - win_y
        print(f"Mouse window: {win_name}")
        print(f"Relative position: x={rel_x}, y={rel_y}")
    else:
        print("Mouse is not within any defined window.")

    # Define the region to capture (left, top, right, bottom)
    region = (x, y, x + length, y + height)

    # Capture the region
    screenshot = ImageGrab.grab(bbox=region)

    # Ensure the 'bb' directory exists
    output_dir = "bb"
    os.makedirs(output_dir, exist_ok=True)

    # Construct the full path for the image
    image_path = os.path.join(output_dir, imagename)

    # Save the image
    screenshot.save(image_path)
    print(f"Image saved at: {image_path}")

def main():
    parser = argparse.ArgumentParser(description="Capture a region of the screen based on mouse position.")
    parser.add_argument("length", type=int, help="The length of the region to capture.")
    parser.add_argument("height", type=int, help="The height of the region to capture.")
    parser.add_argument("imagename", type=str, help="The name of the output image file (e.g., 'image.png').")

    args = parser.parse_args()

    # Capture the specified region
    capture_region(args.length, args.height, args.imagename)

if __name__ == "__main__":
    main()
