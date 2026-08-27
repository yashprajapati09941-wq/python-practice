def withdraw(balance):
    try:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        if amount > balance:
            raise ValueError("Insufficient balance")

        balance = balance - amount

    except ValueError as e:
        print("Error:", e)

    else:
        print("Withdrawal successful!")
        print("Remaining balance:", balance)

    finally:
        print("Thank you for using ATM!")


balance = 5000

withdraw(balance)
