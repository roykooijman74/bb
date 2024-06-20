import argparse
import time

def countdown(duration):
    for i in range(duration, 0, -1):
        print(f"Countdown: {i}         ", end='\r')
        time.sleep(1)
    print("Countdown: 0")

def main():
    parser = argparse.ArgumentParser(description="Countdown timer")
    parser.add_argument("duration", type=int, help="Duration of the countdown in seconds")
    args = parser.parse_args()
    countdown(args.duration)

if __name__ == "__main__":
    main()
