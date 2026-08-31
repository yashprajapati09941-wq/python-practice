def cube(x):
    return x ** 3


numbers = [1, 2, 3, 4, 5]

result = map(cube, numbers)

print(list(result))