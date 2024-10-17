"""TypeCasting ----> It is a way of converting one data type to 
another data type if it is valid

Two types of Typecasting : 
1. Explicit conversion 
2. Implicit conversion 
"""

a = "100"
print("Data Type of a : ", type(a))
# print(a+5)   ---> not valid

print("\nTypecasting of a from string to integer : ")

# Explicit conversion :
a = int(a)
print("\nData Type of a : ", type(a))
print(a + 5)  # Now this a valid

# Implicit converison
p = 4
q = 1.5
print("\nData Type of p : ", type(p))
print("Data Type of q : ", type(q))
print("Data Type of p+q : ", type(p + q))
print(p + q)


# b = "Dilesh"
# b = int(b)   ----> This is not valid

# str(31)      ===> "31"    ---> integer to string
# int("31")    ===> 31      ---> string to integer
# int(31.456)  ===> 31      ---> float to integer
