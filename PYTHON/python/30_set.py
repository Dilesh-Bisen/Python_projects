# Sets : Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.
# Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.


a = {"Carla", 19, False, 5.9, 19}
print(a)
print(type(a))

print("\nThe elements in the set are :")
info = {"Carla", 19, False, 5.9}
for item in a:
    print(item)


print("\nEmpty set : ")
p = set()
# p = {} --> wrong syntax
print("Type of p :",type(p))

