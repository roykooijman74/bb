import sys
import pyautogui

def move_mouse(x, y):
    """Move the mouse to the specified (x, y) coordinates."""
    try:
        pyautogui.moveTo(x, y, duration=0.5)  # Move to the position with a smooth transition
        print(f"Mouse moved to ({x}, {y})")
    except Exception as e:
        print(f"Error moving the mouse: {e}")

def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) != 3:
        print("Usage: python movemouse.py <x> <y>")
        return

    try:
        # Get x and y from command-line arguments
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        
        move_mouse(x, y)
    except ValueError:
        print("Invalid input. Please provide integer values for x and y.")

if __name__ == "__main__":
    main()
