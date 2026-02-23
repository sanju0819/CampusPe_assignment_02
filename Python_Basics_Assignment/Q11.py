# number pattern printer
# user chooses pattern and height

# number pattern printer
# user can choose pattern again and again
# added exit option also


# pattern 1 increasing numbers
def pattern1(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()


# pattern 2 same number repeated in each row
def pattern2(n):
    for i in range(1, n+1):
        for _ in range(i):
            print(i, end=" ")
        print()


# pattern 3  reverse decreasing numbers
def pattern3(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


# pattern 4 palindrome pattern
def pattern4(n):
    for i in range(1, n+1):

        # increasing part
        for j in range(1, i+1):
            print(j, end="")

        # decreasing part
        for j in range(i-1, 0, -1):
            print(j, end="")

        print()


# running menu again and again until user exits
while True:

    print("\nchoose pattern:")
    print("1 increasing numbers")
    print("2 repeated numbers")
    print("3 reverse pattern")
    print("4 palindrome pattern")
    print("5 exit")

    choice = input("enter pattern number: ")

    if choice == "5":
        print("exiting program... ")
        break

    n = int(input("enter height: "))

    if choice == "1":
        pattern1(n)

    elif choice == "2":
        pattern2(n)

    elif choice == "3":
        pattern3(n)

    elif choice == "4":
        pattern4(n)

    else:
        print("wrong choice bro")