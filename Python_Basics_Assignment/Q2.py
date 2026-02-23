# basic calculator
# this does simple math operations on two numbers

try:
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    
    print("sum:", a + b)
    print("difference:", a - b)
    print("product:", a * b)
    
    if b != 0:
        print("division:", a / b)
        print("remainder:", a % b)
    else:
        print("division: can't divide by zero")
        print("remainder: can't divide by zero")
    
    print("exponent:", a ** b)

except:
    print("please enter a valid number")