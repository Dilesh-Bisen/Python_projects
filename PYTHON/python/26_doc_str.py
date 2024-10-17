# Docstrings in Python : Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

print("\nDocstring, right above the function body : ")
def square(n):
    '''It return the square of n''' 
    # always right after the definition of a function
    print(n**2)
square(4)
print(square.__doc__)

print("\nDocstring, not above the function body : ")
def square(n):
    print(n**2)
    '''It return the square of n'''  
square(4)
print(square.__doc__)



# Python Comments : Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

# Python docstrings : As mentioned above, Python docstrings are strings used right after the definition of a function, method, class , or module . They are used to document our code.


# Python doc attribute : Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring.
