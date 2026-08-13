balance = 10000

print("===== ATM MENU =====")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:

    case 1:
        print("Your balance is:", balance)

    case 2:
        deposit = float(input("Enter deposit amount: "))

        if deposit > 0:
            balance = balance + deposit
            print("Amount deposited successfully!")
            print("New balance:", balance)
        else:
            print("Invalid deposit amount")

    case 3:
        withdraw = float(input("Enter withdrawal amount: "))

        if withdraw <= 0:
            print("Invalid withdrawal amount")

        elif withdraw <= balance:
            balance = balance - withdraw
            print("Please collect your cash")
            print("Remaining balance:", balance)

        else:
            print("Insufficient balance")

    case 4:
        print("Thank you for using ATM!")

    case _:
        print("Invalid choice")
        