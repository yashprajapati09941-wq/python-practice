print("-----WELCOME TO KBC-----")
print()

name = input(" Enter your name: ")

print("\nHello", name)
print("Let's start the game!")
print("You will get 5 questions.")
print("Each correct answer = ₹1,000\n")

score = 0


# Question 1
print("Q1. Capital of india?")
print("A. Mumbai")
print("B. Delhi")
print("C. Gujrat")
print("D. Rajasthan")

answer = input("Enter your answer: ")

if answer.lower() == "b":
    print("Correct!")
    score += 1000
else:
    print("Wrong answer!")

print("Your score:", score)
print()

# Question 2
print("Q2. What is 5 + 5?")
print("A. 8")
print("B. 9")
print("C. 10")
print("D. 11")

answer = input("Enter your answer: ")

if answer.lower() == "c":
    print("Correct!")
    score += 1000
else:
    print("Wrong answer!")

print("Your score:", score)
print()


# Question 3
print("Q3. Which one is a programming language?")
print("A. Python")
print("B. Chrome")
print("C. Windows")
print("D. Google")

answer = input("Enter your answer: ")

if answer.lower() == "a":
    print("Correct!")
    score += 1000
else:
    print("Wrong answer!")

print("Your score:", score)
print()


# Question 4
print("Q4. How many days are there in a week?")
print("A. 5")
print("B. 6")
print("C. 7")
print("D. 8")

answer = input("Enter your answer: ")

if answer.lower() == "c":
    print("Correct!")
    score += 1000
else:
    print("Wrong answer!")

print("Your score:", score)
print()


# Question 5
print("Q5. Which keyword is used to create a function in Python?")
print("A. function")
print("B. def")
print("C. fun")
print("D. create")

answer = input("Enter your answer: ")

if answer.lower() == "b":
    print("Correct!")
    score += 1000
else:
    print("Wrong answer!")

print("Your score:", score)
print()



print("-----GAME OVER-----")
print("Player:", name)
print("Final Score: ₹", score)

if score == 5000:
    print("Congratulations! You won the game!")
elif score >= 3000:
    print("Great game!")
else:
    print("Keep practicing!")