# Dictionary methods

student = {
    "name": "Yash",
    "age": 20,
    "marks": 85
}

print("Student:", student)
print()


# get()
print(student.get("name"))
print()


# keys()
print(student.keys())
print()


# values()
print(student.values())
print()


# items()
print(student.items())
print()


# update()
student.update({"marks": 90})
print(student)
print()


# pop()
student.pop("age")
print(student)
print()


# popitem()
student.popitem()
print(student)
print()


# setdefault()
student.setdefault("city", "Ahmedabad")
print(student)
print()


# copy()
new_student = student.copy()
print(new_student)
print()


# fromkeys()
subjects = ["Python", "SQL", "Java"]

new_dict = dict.fromkeys(subjects, "Not Started")
print(new_dict)
print()


# clear()
new_dict.clear()
print(new_dict)