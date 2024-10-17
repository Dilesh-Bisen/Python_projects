'''
Lists : Lists are ordered collection of data items.
    1. They store multiple items in a single variable.
    2. List items are separated by commas and enclosed within square brackets [].
    3. Lists are changeable meaning we can alter them after creation.
'''


marks = [3, 4, 5, "Dilesh", [True,False]]
print(marks)
print("\nAddress of marks :", id(marks))
print("\nType of marks    :", type(marks))

print("\nPositive List Index : ")
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5])  # --> give an error


print("\nNegative List Index : ")
print(marks[-1])  # print(marks[len(marks)-1]) = print(marks[4])
print(marks[-2])
print(marks[-3])
print(marks[-4])
print(marks[-5])
print(marks[1:-1])  # marks[1 : len(marks)-1]


print("\nRange of index :- listName[start : end : jumpIndex]")
print(marks)
print(marks[:])  # print(marks[0:]), print(marks[ : len(marks)])
print(marks[2:4])
print(marks[1:-1]) # marks[1:4]
print(marks[::2])


print("\nCheck whether an item is present in the list : ")
if "Dilesh" in marks:
    print("\nDilesh is present in list of marks.")
else:
    print("\nDilesh is not present in list of marks.")

if 23 in marks:
    print("23 is present in list of marks.")
else:
    print("23 is not present in list of marks.")


if "3" in marks:   # here 3-->string but in list 3-->integer
    print("3 is present in list of marks.")
else:
    print("3 is not present in list of marks.")

# string
if "dil" in "Dilesh":
    print("Yes.")
else:
    print("No.")

# List Comprehension : List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
print("\nList Comprehension : ")

# lst = [i for i in range(5)]
# print(lst)
print([i for i in range(5)])

lst = [i*i for i in range(5)]
print(lst)
lst = [i for i in range(10) if i%2==0]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
print("\n")

c = [(chr(i), i) for i in range(97, 123)]
print(c)
