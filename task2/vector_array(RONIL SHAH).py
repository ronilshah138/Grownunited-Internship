import numpy as np


def main():
    
    values = np.random.randint(1, 101, size=50)

   
    sorted_values = np.sort(values)
    smallest_three = sorted_values[:3]
    largest_three = sorted_values[-3:]

    print("Vector of 50 random values:")
    print(values.tolist())
    print()
    print("Smallest 3 values:", smallest_three.tolist())
    print("Largest 3 values:", largest_three.tolist())


if __name__ == "__main__":
    main()
