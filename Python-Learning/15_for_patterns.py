
# 1. Square Pattern
print("\n1. SQUARE PATTERN")

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


# 2. Increasing Triangle
print("\n2. INCREASING TRIANGLE")

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# 3. Decreasing Triangle
print("\n3. DECREASING TRIANGLE")

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# 4. Number Triangle
print("\n4. NUMBER TRIANGLE")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 5. Same Number Pattern
print("\n5. SAME NUMBER PATTERN")

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


# 6. Reverse Number Pattern
print("\n6. REVERSE NUMBER PATTERN")

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()


# 7. Number Pyramid
print("\n7. NUMBER PYRAMID")

for i in range(1, 6):

    for space in range(5 - i):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()


# 8. Star Pyramid
print("\n8. STAR PYRAMID")

for i in range(1, 6):

    for space in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()


# 9. Reverse Star Pyramid
print("\n9. REVERSE STAR PYRAMID")

for i in range(5, 0, -1):

    for space in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()


# 10. Diamond Pattern
print("\n10. DIAMOND PATTERN")

# Upper half
for i in range(1, 6):

    for space in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()

# Lower half
for i in range(4, 0, -1):

    for space in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()


