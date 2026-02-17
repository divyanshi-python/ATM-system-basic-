balance = 10000
pin = 1234

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    print("Welcome to ATM")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", balance)

        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Updated balance:", balance)

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance")

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Wrong PIN")
