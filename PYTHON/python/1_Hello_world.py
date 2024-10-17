print("\nHello World")


""" 
Module : A module is a file containing code written by somebody else which can be imported and used in our progress.
    1. built in modules ---> os, abc
    2. external modules ---> tensorflow, flask 
    
"""


"""  
Comment : It is a part of the coding file that the programmer does not want to execute .
    1. single line comment    ---> #
    2. multiline line comment ---> """ ''' or """ """
 
'''


"""
Escape sequence character : It is \ followed by the character you want to insert.

"""
print("\nThis is dilesh\nI am a good boy")
# print("my laptop name is "hp" ")    --> invalid
print('\nMy laptop name is "hp" ')
print(" My laptop name is 'hp' ")


"""
Other parameters of print statements : 

1. objects   : Any object and as many as you like will be converted to string before printed.

2. sep = " " : Specify how to seperate objects,if there is more than one. (Default is ' ' i.e. space)

3. end = " " : Specify what to print at the end. (Default is "\n")

4. file : An object with a write method. (Default is sys.stdout)

"""
print("\nDilesh", 1, "fine")
print("\nDilesh", 1, "fine", sep="~", end=" 009\n")
print("Dilesh", 1, "fine", sep="*")

for i in range(6):
    print(i, end=" ")
