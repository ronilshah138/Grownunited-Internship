from pathlib import Path
import numpy as np


def main():
    path = Path(__file__).parent / "temperatures.txt"
    temps = np.loadtxt(path)
    day = int(temps.argmax() + 1)
    hot = temps.max()
    print("Hottest day is day", day, "with", hot, "degrees")


if __name__ == "__main__":
    main()
