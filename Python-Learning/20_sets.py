# Python Set Methods

# Creating sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)


# 1. add()
a.add(10)
print("After add():", a)
print()


# 2. update()
a.update([20, 30])
print("After update():", a)
print()


# 3. remove()
a.remove(10)
print("After remove():", a)
print()


# 4. discard()
a.discard(200)
print("After discard():", a)
print()


# 5. pop()
a.pop()
print("After pop():", a)
print()


# 6. union()
print("Union:", a.union(b))
print()


# 7. intersection()
print("Intersection:", a.intersection(b))
print()


# 8. difference()
print("Difference:", a.difference(b))
print()


# 9. symmetric_difference()
print("Symmetric Difference:", a.symmetric_difference(b))
print()


# 10. issubset()
x = {3, 4}
y = {1, 2, 3, 4, 5}
print("Is subset:", x.issubset(y))
print()


# 11. issuperset()
print("Is superset:", y.issuperset(x))
print()


# 12. isdisjoint()
p = {10, 20}
q = {30, 40}
print("Are disjoint:", p.isdisjoint(q))
print()


# 13. clear()
p.clear()
print("After clear():", p)
print()
