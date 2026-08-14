# Student Marks Analysis

students = int(input("Enter number of students: "))

total_marks = 0
passed = 0
failed = 0
highest = 0
lowest = 100

for i in range(1, students + 1):

    print("\nStudent", i)

    name = input("Enter student name: ")
    marks = int(input("Enter marks (0-100): "))

    total_marks = total_marks + marks

    if marks >= 40:
        passed = passed + 1
        result = "Pass"
    else:
        failed = failed + 1
        result = "Fail"

    if marks > highest:
        highest = marks

    if marks < lowest:
        lowest = marks

    # Grade
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    print("Result:", result)


average = total_marks / students

print("\n===== FINAL RESULT =====")
print("Total Marks:", total_marks)
print("Average Marks:", average)
print("Passed Students:", passed)
print("Failed Students:", failed)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)