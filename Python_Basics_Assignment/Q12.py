# multiplication table generator
# prints table for a number



while True:

    print("\nchoose option:")
    print("1 single table")
    print("2 full table (1-10 grid)")
    print("3 exit")

    ch = input("enter choice: ")

    # exit option
    if ch == "3":
        print("exited")
        break


    # single multiplication table
    elif ch == "1":
        num = int(input("enter number: "))
        rng = int(input("enter range end: "))

        print("\nmultiplication table of", num)

        for i in range(1, rng+1):
            print(f"{num} x {i} = {num*i}")


    # full grid table 
    elif ch == "2":
        print("\nfull table 1 to 10\n")

        for i in range(1, 11):
            for j in range(1, 11):
                print(f"{i*j:4}", end=" ")
            print()


    else:
        print("wrong choice. try again")