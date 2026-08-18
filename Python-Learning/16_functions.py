
# 1. CALCULATE SUM OF NUMBERS

def calculate_sum(numbers):

    total = 0

    for num in numbers:
        total += num

    return total


numbers = [10, 20, 30, 40, 50]

result = calculate_sum(numbers)

print("========== 1: CALCULATE SUM ==========")
print("Numbers:", numbers)
print("Total:", result)

# 2. CHECK THE NUMBER

def check_number(num):

    if num > 0:
        return "Positive"

    elif num < 0:
        return "Negative"

    else:
        return "Zero"


print("\n========== 2: CHECK THE NUMBER ==========")

number = int(input("Enter a number: "))

result = check_number(number)

print("Number is:", result)

# 3. CALCULATE STUDENT GRADE

def calculate_grade(marks):

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 50:
        grade = "C"

    elif marks >= 35:
        grade = "D"

    else:
        grade = "Fail"

    return grade


print("\n========== 3: STUDENT GRADE ==========")

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

grade = calculate_grade(marks)

print("\n----- RESULT -----")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)