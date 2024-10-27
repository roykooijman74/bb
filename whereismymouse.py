import pyautogui
from tabulate import tabulate

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

def find_smurf(x, y):
    """Determine which smurf window the coordinates are in."""
    for smurf in SMURFWINDOWS:
        x1, y1, width, height, name = smurf
        if x1 <= x < x1 + width and y1 <= y < y1 + height:
            return name, x1, y1
    return None, None, None

def is_color_similar(color1, color2, tolerance=25):
    """Check if two RGB colors are similar within a given tolerance."""
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def main():
    """Main function"""
    # Get the current position of the mouse cursor
    x, y = pyautogui.position()

    # Find which smurf window the cursor is in
    smurf_name, smurf_x1, smurf_y1 = find_smurf(x, y)

    # Calculate the relative position to Smurf 1 (top left corner of second screen)
    relative_x = x - smurf_x1
    relative_y = y - smurf_y1

    # Prepare the table data
    table_data = []

    # Get the color of the initial smurf for comparison
    initial_color = pyautogui.pixel(x, y) if smurf_name else (0, 0, 0)

    # Loop through all smurf windows to add their information to the table
    for smurf in SMURFWINDOWS:
        smurf_x, smurf_y, _, _, smurf_label = smurf

        # Calculate the absolute position on the screen for each Smurf
        absolute_x = smurf_x + relative_x
        absolute_y = smurf_y + relative_y

        # Get the color at the calculated absolute coordinates for each smurf window
        try:
            pixel_color = pyautogui.pixel(absolute_x, absolute_y)
        except Exception as e:
            pixel_color = (0, 0, 0)  # Default to black if there's an error getting the color

        # Calculate the differences in R, G, B values
        r_diff = pixel_color[0] - initial_color[0]
        g_diff = pixel_color[1] - initial_color[1]
        b_diff = pixel_color[2] - initial_color[2]

        # Check if the color is similar to the initial smurf color
        color_similar = is_color_similar(pixel_color, initial_color)

        # Highlight the current smurf where the mouse was located
        highlight = "--> " if smurf_label == smurf_name else ""

        # Add the data to the table
        table_data.append([
            f"{highlight}{smurf_label}",
            absolute_x,
            absolute_y,
            f"({pixel_color[0]}, {pixel_color[1]}, {pixel_color[2]})",
            "True" if color_similar else "False",
            r_diff,
            g_diff,
            b_diff
        ])

    # Print the original position, color, and which smurf it is
    if smurf_name:
        print(f"Mouse is in {smurf_name} at position ({x}, {y}) with color {initial_color}")
        print(f"Relative position to {smurf_name}: ({relative_x}, {relative_y})")
    else:
        print("Mouse is not within any defined smurf window.")

    # Display the table without grid
    print("\nTable:")
    print(tabulate(table_data, headers=["Smurf", "Mouse X Absolute", "Mouse Y Absolute", "Color", "Same Color", "R Diff", "G Diff", "B Diff"], tablefmt="plain"))

if __name__ == "__main__":
    main()
