# Online Shopping Cart using While Loop

total = 0

while True:

    print("\n===== SHOPPING MENU =====")
    print("1. Add Laptop - ₹50000")
    print("2. Add Mouse - ₹1000")
    print("3. Add Keyboard - ₹2000")
    print("4. Add Headphones - ₹3000")
    print("5. Show Total")
    print("6. Checkout")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        total = total + 50000
        print("Laptop added to cart.")

    elif choice == 2:
        total = total + 1000
        print("Mouse added to cart.")

    elif choice == 3:
        total = total + 2000
        print("Keyboard added to cart.")

    elif choice == 4:
        total = total + 3000
        print("Headphones added to cart.")

    elif choice == 5:
        print("Your total is: ₹", total)

    elif choice == 6:

        if total == 0:
            print("Your cart is empty!")

        else:
            print("Your total amount is: ₹", total)

            payment = int(input("Enter payment amount: ₹"))

            if payment >= total:
                change = payment - total
                print("Payment successful!")
                print("Your change is: ₹", change)
                print("Thank you for shopping!")
                break

            else:
                print("Insufficient payment!")
                print("You still need: ₹", total - payment)

    else:
        print("Invalid choice!")