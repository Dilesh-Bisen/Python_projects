print("\nDictionary Methods : ")


# update() : The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
print("\nupdate() methods : ")
dict1 = {'name': 'Dilesh', 'age': 19, 'eligible': True}
print(dict1)
dict1.update({'age': 20})    # value change
dict1.update({'DOB': 2001})  # add new item
print(dict1)

dict2 = {110: 50, 111: 60, 112: 70}
dict1.update(dict2)
print(dict1)


# clear() : The clear() method removes all the items from the dictionary.
print("\nclear() methods : ")
dict1 = {'name': 'Dilesh', 'age': 19, 'eligible': True}
dict1.clear()
print(dict1)


# pop() : The pop() method removes the key-value pair whose key is passed as a parameter.
print("\npop() methods : ")
dict1 = {'name': 'Dilesh', 'age': 19, 'eligible': True}
x = dict1.pop('age')
print(x)  # 19
print(dict1)


# popitem() : The popitem() method removes the last key-value pair from the dictionary.
print("\npopitem() methods : ")
dict1 = {'name': 'Dilesh', 'age': 19, 'eligible': True, 'DOB': 2003}
x = dict1.popitem()    # dict1.pop() --> error
print(x)  # 'DOB': 2003
print(dict1)


# del : we can also use the del keyword to remove a dictionary item.
print("\ndel() methods : ")
dict1 = {'name': 'Dilesh', 'age': 19, 'eligible': True, 'DOB': 2003}
del dict1['name']  # or dict1.pop('name')
print(dict1)


# If key is not provided, then the del keyword will delete the dictionary entirely.
# dict1 = {'name': 'Dilesh', 'age': 19, 'eligible': True, 'DOB': 2003}
# del dict1
# print(dict1)
# Output : NameError: name 'dict1' is not defined

print("\n")
d1 = {1:"One",2:"Two"}
d2 = {2:"Three"}
d2.update(d1)
print(d1)
print(d2)