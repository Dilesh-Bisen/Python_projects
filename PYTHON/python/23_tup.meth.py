print("\nTupple Methods : ")

# Manipulating Tupples : Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

print("\nConverting tupple to list :")
num = (1, 2, 3, 4)
temp = list(num)
temp.append("Russia")
temp[2] = 100
num = tuple(temp)
print(num)

print("\nConcatenation of tupple(without converting into list) : ")
num1 = (12, 45, 67, 57)
num2 = (98, 65, 43)
add = num1 + num2
print(add)


# len() method: The len() method of Tuple returns the length of the tupple.
print("\nlen() method : ")
p = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3, 6, 7, 3)
q = len(p)
print("The length of tupple is:", q)


# count() method: The count() method of Tuple returns the number of times the given element appears in the tuple.
print("\ncount() method : ")
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3, 6, 7, 3)
tup = Tuple1.count(3)
print("Count of 3 in Tuple1 is:", tup)


# index() method : The index() method returns the first occurrence of the given element from the tuple.
# Syntax : tuple.index(element, start, end)

print("\nindex() method : ")
tupl = (0, 1, 2, "Dilesh", 4, 5, 7, "Dilesh")
a = tupl.index("Dilesh")

# a = tupl.index("Jack")  --> error(as it is not present)

print("First occurrence of Dilesh is at index :", a)
b = tupl.index("Dilesh", 4, 8)
print("The occurrence of Dilesh between index 4 and 8 is :", b)
