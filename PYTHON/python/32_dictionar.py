'''
Dictionaries : Dictionaries are ordered collection of data items. 
    1.They store multiple items in a single variable.
    2.Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
'''

dict = {'name': 'Dilesh', 'age': 19, 'eligible': True}
print("\nElements of dictionary : ", dict)
print("\nType of dictionary : ", type(dict))


print("\nAccessing Dictionary items :")

# I. Accessing keys : We can print all the keys in the dictionary using keys() method.
print("\nAccessing keys :")
print(dict.keys())
print("Type of dict.keys() :", type(dict.keys()))


# II. Accessing single values : Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.
print("\nAccessing single values :")
# print(dict['name']) # or
print(dict.get('name'))

# print(dict['address'])      --->show error if not exist
print(dict.get('address'))  # do not show error ,o/p = None


# III. Accessing multiple values : We can print all the values in the dictionary using values() method.
print("\nAccessing multiple values :")
print(dict.values())
print("Type of dict.values() :", type(dict.values()))


# IV. Accessing key-value pairs : We can print all the key-value pairs in the dictionary using items() method.
print("\nAccessing key-value pairs :")
print(dict.items())
print("Type of dict.items() :", type(dict.items()))


print("\n")
for i in dict.keys():
    print(i)
for i in dict.keys():
    print(dict[i])
    
    
print("\n")
for key in dict.keys():
    print(f"The value corresponding to the {key} is {dict[key]}")
    
    
print("\n")
for key,value in dict.items():
    print(f"The value corresponding to the {key} is {value}")