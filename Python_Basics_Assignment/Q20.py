# Number System Functions Program
# contains different mathematical utility functions

# 1. factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 2. check prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 3. nth fibonacci number
def fibonacci(n):
    if n <= 0:
        return "Enter positive position"
    if n == 1:
        return 0
    if n == 2:
        return 1

    a = 0
    b = 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b


# 4. sum of digits
def sum_of_digits(n):
    total = 0
    for digit in str(abs(n)):   # handle negative numbers
        total += int(digit)
    return total


# 5. reverse number
def reverse_number(n):
    rev = 0
    sign = -1 if n < 0 else 1
    n = abs(n)

    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10

    return sign * rev


# 6. armstrong number check
def is_armstrong(n):
    num_str = str(abs(n))
    power = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** power

    return total == abs(n)


# 7. gcd using loop method
def gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b
    return a


# 8. lcm using gcd
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


# 9. perfect number check
def is_perfect_number(n):
    if n <= 0:
        return False

    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


# 10. menu function
def math_menu():

    while True:
        print("\n===== NUMBER SYSTEM MENU =====")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci (nth)")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "10":
            print("Program ended.")
            break

        if choice == "1":
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif choice == "2":
            n = int(input("Enter number: "))
            if is_prime(n):
                print("It is a PRIME number")
            else:
                print("Not a prime number")

        elif choice == "3":
            n = int(input("Enter position: "))
            print("Fibonacci number:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter number: "))
            if is_armstrong(n):
                print("It is an Armstrong number")
            else:
                print("Not an Armstrong number")

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter number: "))
            if is_perfect_number(n):
                print("It is a Perfect number")
            else:
                print("Not a Perfect number")

        else:
            print("Invalid choice. Try again.")


# run the program
math_menu()