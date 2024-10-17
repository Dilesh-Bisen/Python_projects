# String is one of the data type in python
# It is a sequence of character enclosed in a quotes

# String Function
story = "\nOnce upon a time there was a boy who opened a youtube channel"
print(story)
print("Length of a string : ", len(story))

a = "Dilesh"
print("\n", a)
print(type(a), "\n")

# b = '''Hello'''  ---> triple quote
# b = "Hello"      ---> double quote
# b = 'Hello'      ---> single quote

# p = 'Dilesh's'  , It is invalid syntax
p = "Dilesh's"  # It is valid syntax
print(p)
q = 'Dilesh"s'
print(q)
r = """Dilesh's and Dilesh"s """
print(r, "\n")

a = "Good Morning, "
b = "Dilesh"
c = a + b  # Concatenating two strings
print(c)
# b[4] = 'z'   ---> can`t change doesn`t work

print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])
# print(b[6]) it will throw an error

print("\nLets use a for loop :")
for character in a:
    print(character)
