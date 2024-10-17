# Recursion in python : Recursion is the process of defining something in terms of itself.

# Python Recursive Function : In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

print("\nFactorial function : ")
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return n * factorial(n-1)
print("The factorial of 5 is :", factorial(5))


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 38,
print("\nFibbonacci series function : ")  # f0=0,f1=1, f2= f1+f0
def fibbo(n):
    # if (n == 0):
    #     return 0
    # elif (n == 1):
    #     return 1
    if (n <= 1):
        return n
    else:
        return fibbo(n-1) + fibbo(n-2)
print(fibbo(3))
