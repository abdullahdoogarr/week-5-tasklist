# Task 2: ATM Withdrawal Simulation

balance = 50000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    choice = input("Select an option (1-4): ").strip()

    if choice == "1":
        print(f"Your current balance is Rs. {balance:,.2f}")

    elif choice in ("2", "3"):
        try:
            amount = float(input("Enter amount: Rs. "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero. Transaction rejected.")
        elif choice == "2":
            balance += amount
            print(f"Deposited Rs. {amount:,.2f}. New balance: Rs. {balance:,.2f}")
        elif amount > balance:
            print("Insufficient balance. Withdrawal rejected.")
        else:
            balance -= amount
            print(f"Withdrew Rs. {amount:,.2f}. New balance: Rs. {balance:,.2f}")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-4.")
