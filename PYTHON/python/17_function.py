a = 1
b = 4
arithmetic_mean1 = (a + b) / 2
print("Arithmetic mean of 1 and 4 = ", arithmetic_mean1)

c = 8
d = 2
arithmetic_mean2 = (c + d) / 2
print("Arithmetic mean of 8 and 2 = ", arithmetic_mean2)

# or

print("\nFunctions in python : ")



# return Statement : The return statement is used to return the value of the expression back to the calling function.
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
a = name("James", "Buchanan", "Barnes")
print(a)

# def arithmetic_mean(a, b):
#     return (a+b)/2
# x = int(input("\nEnter first number  : "))
# y = int(input("Enter second number : "))
# z = arithmetic_mean(x, y)    ---> here, return the value for z
# print(z)



def arithmetic_mean(a, b):
    print((a+b)/2)

def isGreater(p, q):
    if (p > q):
        print(p, "is greater than", q)
    elif (p == q):
        print(p, "is equal to", q)
    else:
        print(q, "is greater than", p)

def isLesser(p, q):
    pass
    # if (p < q):
    #     print(p, "is less than", q)
    # elif (p == q):
    #     print(p, "is equal to", q)
    # else:
    #     print(q, "is less than", p)

x = int(input("\nEnter first number  : "))
y = int(input("Enter second number : "))
arithmetic_mean(x, y)
isGreater(x, y)

