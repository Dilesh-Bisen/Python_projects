print("\nList Methods : ")

# 1. list.sort() : This method sorts the list in ascending order. The original list is updated.
print("\n1. list.sort() : ")
num = [45, 67, 12, 34, 98, 55, 22]
num.sort()
print(num)

colors = ["voilet", "indigo", "blue", "green"]
# print(colors.sort()) --> will return None
colors.sort()
print(colors)


print("\n2. list.sort(reverse=True) : ")
num = [45, 67, 12, 34, 98, 55, 22]
num.sort(reverse=True)
print(num)


# append()  :This method appends items to the end of the existing list.
print("\n3. list.append() : ")
colors = [33, 42, 67, 82, 10, 99, 22]
colors.append(100)
print(colors)
print(colors.append(100))


# reverse() : This method reverses the order of the list.
print("\n4. list.reverse() : ")
num = [11, 72, 37, 45, 15, 56, 87, 38, 99]
num.reverse()
print(num)


# index() : This method returns the index of the first occurrence of the list item.
print("\n5. list.index() : ")
num = [67, 83, 46, 11, 69, 73, 97, 19]
print("The index of 97 in the list is", num.index(97))


# count() : Returns the count of the number of items with the given value.
print("\n6. list.count() : ")
num = [4, 2, 5, 3, 6, 1, 2, 1, 3, 2, 8, 9, 7, 1]
print(num.count(1))


# copy() : Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
print("\n7. list.copy() : ")
m = ["voilet", "green", "indigo", "blue"]
n = m.copy()
print(m)
print(n)


# insert(): This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
print("\n8. list.insert() : ")
num = [67, 83, 46, 11, 69, 73, 97, 19]
colors.insert(1, 100)  # inserts item at index 1
print(colors)


# extend(): This method adds an entire list or any other collection datatype(set, tuple, dictionary) to the existing list i.e., add a list to a list
print("\n9. list.extend() : ")
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
a.extend(b)
print(a)
a = [1, 2, 3, 4, 5]
b = "Dilesh"
a.extend(b)
print(a)


# Concatenating two lists: You can simply concatenate two lists to join two lists.
print("\n9. list concatenation : ")
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
c = a + b
print(c)  # here,new list formed but in extend() list is changed
