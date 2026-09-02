from functools import reduce

numbers = [10, 20, 30, 40, 50]  # List

def add(a, b):                  # Function
    return a + b                # Addition

result = reduce(add, numbers)   # Reduce

print(result)                   # Output


from functools import reduce

numbers = [1, 2, 3, 4, 5]

def multiply(a, b):
    return a * b

result = reduce(multiply, numbers)

print(result)