a = int(input("\nEnter your age : "))
print("Your age is",a)


# Indentation : Python uses four spaces as default indentation spaces. However, the number of spaces can be anything; it is up to the user. But a minimum of one space is needed to indent a statement.

if(a>18):
    print("\nYou can drive.")
    print("Yes")
else:
    print("\nYou cannot drive.")
    print("No")
print("Yahoo\n ")


# Conditional/comparison operator in python : 
# >, <, >=, <=, ==, !=
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)

apple_price = 10
budget = 200
if(budget - apple_price > 70) :
    print("\nSiri, add 5kg apples to the cart.")
elif(budget - apple_price > 50) :
    print("\nSiri, add 1kg apples to the cart.")
else :
    print("\nSiri, do not add apples to the cart.")

num = int(input("\nEnter a value : "))

if(num < 0):
    print("Number is negative.")
elif(num == 0):
    print("Number is Zero.")
elif(num == 1):
    print("Number is Special.")
else:
    print("Number is positive.")
    
print("I am fine.")


# Nested if-else statement : 

val = 20

if(val < 0):
    print("\nNumber is negative.")
elif(val > 0):
    if(val <= 10):
        print("\nNumber is between 1-10.")
    elif(val > 10 and val <= 30):
        print("\nNumber is between 11-30.")
    else:
        print("\nNumber is greater than 30.")
else:
    print("\nNumber is Zero.")
    
