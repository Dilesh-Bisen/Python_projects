# A variable is a name given to a memory location in a program or it is a container which holds the data.

print(
    """\nRules for Python variables:
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and 
   underscores(A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three 
   different variables)\n"""
)

a = 30
b = "Dilesh"
c = 45.32

print(a)
print(b)
print(c)


# Keywords are reserved words that can not be used as a variable name, function name, or any other identifier.
import keyword

print("\nThe list of keywords is : \n")
print(keyword.kwlist)


# Identifier is a user-defined name given to a variable, function, class, module, etc. The identifier is a combination of character digits and an underscore. They are case-sensitive i.e., 'num' and 'Num' and 'NUM' are three different identifiers in python.
