

# This program will calculate the factorial of a number
# Factorial means multiplying all numbers from 1 to n

print("Welcome to Factorial Calculator Program")
print("=========================================")

# using while loop so that program keeps running until user wants to exit
while True:

    
    print("")
    print("MENU:")
    print("1 - Calculate Factorial")
    print("2 - Exit Program")
    print("")

    ch = input("Enter your choice (1 or 2): ")

    # if user press 2 then exit
    if ch == "2":
        print("Thank you! Exiting program...")
        break

    # if user press 1 the calculate
    elif ch == "1":

        num = input("Enter any number: ")

        # check if input is empty
        if num == "" or num == " ":
            print("You did not enter anything. Please try again.")
            continue

        # checking if number is valid or not using try except
        try:
            n = int(num)
        except:
            print("Wrong input! Please enter a number only.")
            continue

        # factorial not possible for negative number
        if n < 0:
            print("Error: Negative number not allowed!")
            continue

        # special case: 0! = 1 (this is mathematical rule)
        if n == 0:
            print("Answer: 0! = 1")
            continue

        # now calculating factorial using for loop
        result = 1  # starting result from 1
        
        # loop will run from 1 to n
        for i in range(1, n + 1):
            result = result * i  # multiplying each number

        # printing the final answer
        print("")
        print("Factorial of", n, "is =", result)
        print("That means", n, "! =", result)

    # if user enters wrong choice
    else:
        print("Wrong choice! Please enter 1 or 2 only.")