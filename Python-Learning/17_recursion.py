
# Example 1: Count Down Using Recursion

def count(n):
    if n == 0:
        return

    print(n)
    count(n - 1)


print("Example 1: Count Down")
count(5)


# Example 2: Factorial Using Recursion

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print("\nExample 2: Factorial")

num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial:", result)