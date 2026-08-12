# Python String Functions

name = "Tyler durden never exsist"

# 1. len() - String's latter count with space
print(len(name))

# 2. upper() - Capital letters
print(name.upper())

# 3. lower() - Small letters
print(name.lower())

# 4. capitalize() - First letter capital
print(name.capitalize())

# 5. title() -  word's first letter capital
print(name.title())

# 6. replace() - Text replace 
print(name.replace("Tyler", "Mohan"))

# 7. count() -  Specific letter count  
print(name.count("t"))

# 8. find() - Character/word's position find karna
print(name.find("never"))

# 9. startswith() - Check starting of the string  
print(name.startswith("yash"))

# 10. endswith() - Check ending of the string
print(name.endswith("yash"))

# 11. strip() - Extra spaces remove 
text = "   Hello Python   "
print(text.strip())

# 12. split() 
print(name.split())