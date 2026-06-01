import math

while True:
    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Floor Division")
    print("8. Square")
    print("9. Cube")
    print("10. Square Root")
    print("11. Greater Number")
    print("12. Smaller Number")
    print("13. Even or Odd")
    print("14. Percentage")
    print("15. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 15:
        print("Calculator Closed!")
        break

    elif choice in [1, 2, 3, 4, 5, 6, 7, 11, 12]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", a + b)

        elif choice == 2:
            print("Result =", a - b)

        elif choice == 3:
            print("Result =", a * b)

        elif choice == 4:
            if b != 0:
                print("Result =", a / b)
            else:
                print("Cannot divide by zero")

        elif choice == 5:
            print("Result =", a % b)

        elif choice == 6:
            print("Result =", a ** b)

        elif choice == 7:
            print("Result =", a // b)

        elif choice == 11:
            print("Greater Number =", max(a, b))

        elif choice == 12:
            print("Smaller Number =", min(a, b))

    elif choice == 8:
        n = float(input("Enter a number: "))
        print("Square =", n ** 2)

    elif choice == 9:
        n = float(input("Enter a number: "))
        print("Cube =", n ** 3)

    elif choice == 10:
        n = float(input("Enter a number: "))
        print("Square Root =", math.sqrt(n))

    elif choice == 13:
        n = int(input("Enter a number: "))
        if n % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")

    elif choice == 14:
        total = float(input("Enter total marks/value: "))
        obtained = float(input("Enter obtained value: "))
        print("Percentage =", (obtained / total) * 100, "%")

    else:
        print("Invalid Choice")