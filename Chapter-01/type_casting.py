# type() FUNCTION AND TYPE CASTING


# PART 1: type() FUNCTION

# We create a variable
age = 21

# Print the value
print("Age:", age)
print("Datatype of age:", type(age))


# PART 2: TYPE CASTING

# We have the same value again
age = 21

# Convert integer into float
age_float = float(age)

print("\nOriginal age:", age)
print("Original datatype:", type(age))

print("After type casting:", age_float)
print("New datatype:", type(age_float))


# PART 3: STRING TO INTEGER

# Here, 21 is stored as a string
age = "21"

print("\nAge:", age)
print("Datatype before casting:", type(age))

# Convert string into integer
age_int = int(age)

print("Age after casting:", age_int)
print("Datatype after casting:", type(age_int))


# PART 4: INTEGER TO STRING

age = 21

print("\nAge:", age)
print("Datatype before casting:", type(age))

# Convert integer into string
age_string = str(age)

print("Age after casting:", age_string)
print("Datatype after casting:", type(age_string))


# PART 5: FLOAT TO INTEGER

age = 21.5

print("\nAge:", age)
print("Datatype before casting:", type(age))

# Convert float into integer
age_int = int(age)

print("Age after casting:", age_int)
print("Datatype after casting:", type(age_int))