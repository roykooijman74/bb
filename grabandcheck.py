import os
import argparse
from functools import partial
import pyautogui
from PIL import Image, ImageGrab
from tabulate import tabulate

# Configure ImageGrab to grab from all screens
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

# List of all windows (Smurfs) with coordinates and names
SMURFWINDOWS = [
    [2560, 0, 790, 460, "Smurf 1"],
    [3414, 0, 790, 460, "Smurf 2"],
    [4267, 0, 790, 460, "Smurf 3"],
    [2560, 461, 790, 460, "Smurf 4"],
    [3414, 461, 790, 460, "Smurf 5"],
    [4267, 461, 790, 460, "Smurf 6"],
    [2560, 921, 790, 460, "Smurf 7"],
    [3414, 921, 790, 460, "Smurf 8"],
    [4267, 921, 790, 460, "Smurf 9"],
    [1770, 0, 790, 460, "A Supersmurf"],
    [1770, 461, 790, 460, "B MiniSmurf"],
    [1770, 921, 790, 460, "C KickSmurf"],
]

def find_window_by_position(x, y):
    for window in SMURFWINDOWS:
        win_x, win_y, width, height, name = window
        if win_x <= x < win_x + width and win_y <= y < win_y + height:
            return window
    return None

def image_matches(region, target_image):
    """Check if the given region matches the target image."""
    screenshot = ImageGrab.grab(bbox=region)
    screenshot = screenshot.convert("RGB")
    target_image = target_image.convert("RGB")
    return screenshot == target_image

def capture_and_check(x, y, length, height, target_image_path):
    # Define the region to capture (left, top, right, bottom)
    region = (x, y, x + length, y + height)

    # Capture the region
    screenshot = ImageGrab.grab(bbox=region)

    # Ensure the 'captured_images' directory exists
    output_dir = "captured_images"
    os.makedirs(output_dir, exist_ok=True)

    # Save the captured image
    captured_image_path = os.path.join(output_dir, "captured_image.png")
    screenshot.save(captured_image_path)
    print(f"Captured image saved at: {captured_image_path}")

    # Load the target image
    target_image = Image.open(target_image_path)

    # Find the Smurf window containing the mouse position
    window = find_window_by_position(x, y)
    smurf_name, rel_x, rel_y = "None", None, None
    if window:
        win_x, win_y, _, _, smurf_name = window
        rel_x, rel_y = x - win_x, y - win_y

    # Prepare table data
    table_data = []

    for smurf in SMURFWINDOWS:
        smurf_x, smurf_y, width, height, smurf_label = smurf
        region = (smurf_x + rel_x, smurf_y + rel_y, smurf_x + rel_x + length, smurf_y + rel_y + height)

        # Check if the target image matches this region
        try:
            matches = image_matches(region, target_image)
        except Exception:
            matches = False

        # Highlight the current Smurf window
        highlight = "--> " if smurf_label == smurf_name else ""

        # Add data to the table
        table_data.append([
            f"{highlight}{smurf_label}",
            f"({smurf_x}, {smurf_y})",
            matches
        ])

    # Print results
    print(f"Mouse Position: ({x}, {y})")
    print(f"Relative Position to {smurf_name}: ({rel_x}, {rel_y})" if window else "Mouse is not within any defined Smurf window.")
    print("\nResults:")
    print(tabulate(table_data, headers=["Smurf", "Position", "Image Matches"], tablefmt="plain"))

def main():
    parser = argparse.ArgumentParser(description="Capture a region and check against all Smurf windows.")
    parser.add_argument("length", type=int, help="The length of the region to capture.")
    parser.add_argument("height", type=int, help="The height of the region to capture.")
    parser.add_argument("imagename", type=str, help="The path to the target image file (e.g., 'target.png').")

    args = parser.parse_args()

    # Get the current mouse position
    x, y = pyautogui.position()

    # Perform the capture and check
    capture_and_check(x, y, args.length, args.height, args.imagename)

if __name__ == "__main__":
    main()