
# Problem 1: Print numbers from 1 to N

def count_up(n):
    if n == 0:
        return

    count_up(n - 1)
    print(n)


print("Problem 1: Numbers from 1 to N")

num = int(input("Enter a number: "))
count_up(num)


# Problem 2: Print numbers from N to 1

def count_down(n):
    if n == 0:
        return

    print(n)
    count_down(n - 1)


print("\nProblem 2: Numbers from N to 1")

num = int(input("Enter a number: "))
count_down(num)


# Problem 3: Sum of numbers from 1 to N

def sum_numbers(n):
    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


print("\nProblem 3: Sum from 1 to N")

num = int(input("Enter a number: "))

result = sum_numbers(num)

print("Sum:", result)


# Problem 4: Factorial of a number


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("\nProblem 4: Factorial")

num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial:", result)

# Problem 5: Sum of digits

def sum_digits(n):
    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)


print("\nProblem 5: Sum of Digits")

num = int(input("Enter a number: "))

result = sum_digits(num)

print("Sum of digits:", result)