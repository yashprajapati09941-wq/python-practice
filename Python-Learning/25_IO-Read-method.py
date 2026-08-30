# Read

file = open("student.txt", "r")

# Check
print(file.readable())
print(file.writable())

# Position
print(file.tell())

# Read
print(file.read())

# Move
file.seek(0)

# Line
print(file.readline())
print(file.readline())

# Move
file.seek(0)

# Lines
print(file.readlines())

# Close
file.close()

# Status
print(file.closed)