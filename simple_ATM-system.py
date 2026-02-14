balance = 10000
pin = 1234

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    print("Welcome to ATM")

    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

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

    else:
        print("Invalid choice")

else:
    print("Wrong PIN")




