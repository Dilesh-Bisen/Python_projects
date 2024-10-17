""" Data Types in Python : It specify the type of data that can 
    be stored inside a variable.
1. Numeric data  : int, float, complex
2. Text data     : string
3. Boolean data 
4. Sequence data : list, tupple
6. Map data      : dictionary
5. None

"""

a1 = 30
a2 = 45.32
a3 = complex(1, 2)
b = """Dilesh"""
# b = "Dilesh"
# b = 'Dilesh'
c1 = True
c2 = False
d = None
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
dict1 = {"name": "Dilesh", "age": 20, "canVote": True}


print("\nPrinting the Variables : ")
print(a1)
print(a2)
print(a3)
print(b)
print(c1)
print(c2)
print(d)
print(list1)
print(tuple1)
print(dict1)


print("\nPrinting the data types of variables : ")
print(type(a1))
print(type(a2))
print(type(a3))
print(type(b))
print(type(c1))
print(type(c2))
print(type(d))
print(type(list1))
print(type(tuple1))
print(type(dict1))
