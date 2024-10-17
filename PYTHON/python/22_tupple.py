'''
Tuples : They are ordered collection of data items. 
    1. They store multiple items in a single variable. 
    2. Tuple items are separated by commas and enclosed within 
    round brackets (). 
    3. Tuples are unchangeable meaning we can not alter them 
    after creation.
'''

tup = (1, 4, 7, "Dilesh", True)
print("Type of tup     :", type(tup))
print("Length of tup   :", len(tup))
print("Elements of tup :", tup)
 
# I. Positive Indexing : As we have seen that tuple items have index, as such we can access items using these indexes.
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
# print(tup[4])   not present so error occur
 
# II. Negative Indexing : Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index[-1], second last item has index[-2], third last item has index[-3] and so on.
print(tup[-2])   # or tup(len(tup) -1 )
print("\n")

tup = (56)   # not valid for tupple write instead tupple = (56,)
print(tup)
print("Type of tup :", type(tup))
tup = (56,)   # now valid
print(tup)
print("Type of tup :", type(tup))


# Tuples are unchangeable meaning
tup = (1, 4, 7)
# tup[0] = 3  ---> provide an error
# print(tup)

# List are changeable meaning
lst = [1, 4, 7]
lst[0] = 3  # ---> will not provide an error
# print(tup)

# III. Check for item : We can check if a given item is present in the tuple. This is done using the in keyword.
tupl = ('Abhijeet', 18, 'FYB', 9.8)

if 18 in tupl:
    print("\nYes,present.")
else:
    print("\nNo,not present.")

if "Dilesh" in tupl:
    print("Yes,present.")
else:
    print("No,not present.")
print("\n")

# IV. Range of Index : You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range. Syntax:Tuple[start: end: jumpIndex]

animals = ("cat", "dog", "bat", "mouse", "pig", "horse")
print(animals[:])  # animals[0:] or animals[:len(animals)]
print(animals[3:6])
# ani = animals[3:6]  same as above
# print(ani)
print(animals[-5:-1]) # animals[len(animals)-5 : len(animasl)-1]
print("\n")

c = [(chr(i), i) for i in range(97, 123)]
print(c)
print("\n")
for i in c:
    print(i[0], end=" ")

print("\n",type(i))
