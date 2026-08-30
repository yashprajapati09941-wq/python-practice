# Write

file = open("student.txt", "w")

# Check
print(file.writable())
print(file.readable())

# Write
file.write("Mohan\n")
file.write("Python\n")
file.write("SQL\n")

# Lines
data = ["HTML\n", "CSS\n", "JavaScript\n"]
file.writelines(data)

# Position
print(file.tell())

# Close
file.close()

# Status
print(file.closed)