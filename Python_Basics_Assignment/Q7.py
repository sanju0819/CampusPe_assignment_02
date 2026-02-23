# temperature converter - menu based system

while True:
    # display all conversion options
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", (c * 9/5) + 32)

    elif ch == "2":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", (f - 32) * 5/9)

    elif ch == "3":
        c = float(input("Enter Celsius: "))
        print("Kelvin:", c + 273.15)

    elif ch == "4":
        k = float(input("Enter Kelvin: "))
        print("Celsius:", k - 273.15)

    elif ch == "5":
        f = float(input("Enter Fahrenheit: "))
        # convert F to C first, then add 273.15 to get Kelvin
        print("Kelvin:", (f - 32) * 5/9 + 273.15)

    elif ch == "6":
        k = float(input("Enter Kelvin: "))
        # convert K to C first, then apply C to F formula
        print("Fahrenheit:", (k - 273.15) * 9/5 + 32)

    elif ch == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again")