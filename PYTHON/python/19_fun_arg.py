'''
There are four types of arguments that we can provide in a function:

    1. Default Arguments
    2. Keyword Arguments
    3. Required Arguments
    4. Variable length Arguments

'''

# 1. Default arguments :   We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

print("\nDefault arguments :\n")


def aver(x=5, y=7):  # here x=5 and y=7 are default arguments
    print((x+y)/2)
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
aver(a, b)

aver(9)   # here only a = 9 and b will be y=7
aver(x=9)  # here b = 9 and a will be x = 5
aver()  # automatically a = x and b = y


def name1(fname, mname="S", lname="Bisen"):
    print("Hello,", fname, mname, lname)
name1("Dilesh")  # here fname = "Dilesh"


# 2.Keyword arguments : We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

print("\n\nKeyword arguments :")


def avg(x=5, y=7):  # here x=5 and y=7 are default arguments
    print((x+y)/2)
avg(y=8, x=4)


def name2(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name2(mname="S", lname="Bisen", fname="Dilesh")


# 3. Required arguments : In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

print("\n\nRequired arguments :")


def sum(a, b, c=1):
    print(a+b+c)
sum(2, 3)


def name3(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name3("Dilesh", "S", "Bisen")
# name3("Dilesh", "S") --> will show an error


# 4. Variable-length arguments : Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
'''
There are two ways to achieve this:

Arbitrary Arguments :
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

Keyword Arbitrary Arguments :
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

'''

print("\n\nVariable-length arguments :")

print("\nArbitrary Arguments:")
def average1(*numbers):
    print("Type of numbers : ", type(numbers))
    sum = 0
    for i in numbers:
        sum+=i
    print(sum/len(numbers))
average1(1,2,3,4,5)


def name(*names):
    for i in names:
        print(i)
name("James", "Buchanan", "Barnes")



print("\nKeyword Arbitrary Arguments:")

def name(**names):
    print("Type of names : ", type(names))
    print(names["fname"], names["mname"], names["lname"])
name(fname="James", mname="Buchanan", lname="Barnes" )



def f():
    print(s)
    s+="perl"
    print(s)
s = "python"
f()
print(s)