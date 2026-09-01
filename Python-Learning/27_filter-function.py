numbers = [10, 15, 20, 25, 30, 35, 40]

def even(num):
    return num % 2 == 0

result = filter(even, numbers)

print(list(result))