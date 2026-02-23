# ATM Simulator

balance = 10000  # starting balance

while True:
    print("\n--- ATM SIMULATOR ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print(f"Current Balance: ₹{balance}")

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Enter a valid amount.")
        else:
            balance += amount
            print(f"₹{amount} deposited successfully! New balance: ₹{balance}")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > balance:
            print("Insufficient balance!")
        elif (balance - amount) < 500:  # minimum ₹500 must remain
            print("Cannot withdraw! Minimum balance of ₹500 must be maintained.")
        else:
            balance -= amount
            print(f"Withdrawal successful! New balance: ₹{balance}")

    elif choice == 4:
        print("Thank you for using ATM. Goodbye!")
        break  # exit the loop

    else:
        print("Invalid choice! Please enter 1-4.")
