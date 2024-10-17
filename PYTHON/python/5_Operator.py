""" Operators in Python

1. Arithmetic operators
2. Assignment operators
3. Logical    operators
4. Comparison operators

"""
# a = 10 ; b = 4  or
a = 10
b = 4


print("\nArithmetic Operators : \n")

# addition operator
print("The value of a + b is   : ", a + b)
# substraction operator
print("The value of a - b is   : ", a - b)
# multiplication operator
print("The value of a * b is   : ", a * b)
# division operator
print("The value of a / b is   : ", a / b)
# floor divison operator
print("The value of a // b is  : ", a // b)
# modulus operator
print("The value of a % b is   : ", a % b)
# exponential operator
print("The value of a ** b is  : ", a**b)
print("\n")

print("\nAssignment Operators : \n")

x = 2
print(x)

x += 1
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 4
print(x)

print("\n")


print("\nLogical Operators :\n")

bool_1 = True
bool_2 = False

print("The value of bool_1 and bool_2 is : ", bool_1 and bool_2)
print("The value of bool_1 or bool_2 is  : ", bool_1 or bool_2)
print("The value of not bool_1 is   : ", not bool_1)
print("\n")


print("\nComparison Operators : \n")

m = 4
n = 9

print("The value of m is greater than n             : ", m > n)
print("The value of m is less than n                : ", m < n)
print("The value of m is greater than or equal to n : ", m >= n)
print("The value of m is less than or equal to n    : ", m <= n)
print("The value of m is equal to n                 : ", m == n)
print("The value of m is not equal to  n            : ", m != n)
print("\n")


p = 3
q = 6
r = 5
print(p * q / r // p)
