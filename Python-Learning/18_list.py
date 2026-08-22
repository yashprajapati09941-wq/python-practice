list=["mohan", 456, "pyare", 67]
list1=[31,15,56,19,34]
list2=["mango", "banana", "tomato", "lichi"]

 #List are mutalbe

list[0]="mohandas"       
print(list)


#list methods:

print(" \n-----1.Append Method-----")

list.append(6)
list2.append("orange")
print(list)
print(list2)

print(" \n-----2.Sort Method-----")

list1.sort()
print(list1)

list2.sort()
print(list2)

print(" \n-----3.Decresing sorting  Method-----")

list1.sort(reverse=True)
print(list1)

list2.sort(reverse=True)
print(list2)

print(" \n-----3.Reverse Method-----")
list1.reverse
print(list1)

list2.reverse
print(list2)

print(" \n-----4.Insert Method-----")

list1.insert(2,345)
print(list1)

list2.insert(2,"apple")
print(list2)

print(" \n-----5.remove Method-----")

list1.remove(31)
print(list1)

list2.remove("lichi")
print(list2)

print(" \n-----6.Pop Method-----")

list1.pop(2)
print(list1)

list2.pop(3)
print(list2)


