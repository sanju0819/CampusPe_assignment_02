# Calculator using functions
# simple menu driven calculator

# addition
def add(a, b):
    return a + b

# subtraction
def subtract(a, b):
    return a - b

# multiplication
def multiply(a, b):
    return a * b

# division
def divide(a, b):
    # cannot divide by zero
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# modulus
def modulus(a, b):
    if b == 0:
        return "Error: Cannot perform modulus with zero"
    return a % b

# power
def power(a, b):
    return a ** b


# main calculator
def calculator():

    while True:
        print("\n===== CALCULATOR MENU =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice: ")

        # exit option
        if choice == "7":
            print("Calculator closed.")
            break

        # validate choice
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please select correct option.")
            continue

        # take number inputs safely
        num1_input = input("Enter first number: ")
        num2_input = input("Enter second number: ")

        # check empty input
        if num1_input.strip() == "" or num2_input.strip() == "":
            print("Input cannot be empty.")
            continue

        # validate numbers (allow negative and decimal)
        try:
            a = float(num1_input)
            b = float(num2_input)
        except:
            print("Invalid number entered. Please enter valid numeric values.")
            continue

        # perform operation
        if choice == "1":
            print("Result:", add(a, b))

        elif choice == "2":
            print("Result:", subtract(a, b))

        elif choice == "3":
            print("Result:", multiply(a, b))

        elif choice == "4":
            print("Result:", divide(a, b))

        elif choice == "5":
            print("Result:", modulus(a, b))

        elif choice == "6":
            print("Result:", power(a, b))


# calling main function
calculator()