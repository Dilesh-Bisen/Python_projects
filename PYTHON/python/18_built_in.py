print("\nAbsolute Value : ")
a = 12
b = -4
c = 3+4j
d = 7.90
print(abs(a), abs(b), abs(c), abs(d), sep="   ")


print("\nSum : ")
num = [2.5, 3, 4, -5]
print(sum(num))  # print(sum(1,2)) is invalid


print("\nType : ")
a1 = 30
a2 = 45.32
a3 = complex(1, 2)
print(type(a1), type(a2), type(a3), sep="   ")


print("\nReversed in loop : ")
for i in reversed(range(10)):
    print(i,end=' ')
# print("\n")


print("\n\nDecimal to binary : ")
a=5
print(bin(a))


print("\nRound off : ")
print(round(4.2))
print(round(4.5))
print(round(4.7))


print("\nBoolean value : ")
print(bool(0), bool(None), bool(-4.5), bool("False"), bool("True"), sep="  ")


print("\nLength of a string : ")
print(len("Hello, I am Dilesh."))


print("\nMaximum : ")
num = [11, 13, 12, 15, 14]
print('Maximum is:', max(num))


print("\nMinimum : ")
print(min(2, 5, 3, 1, 99))
# num = [2, 5, 3, 1, 99]
# print('Minimum is:', min(num))


print("\nPower function : ")
print(pow(2,3))
print(pow(2,4.5))
print(pow(3,-1))


print("\nSorting : ")
arr = (3,6,2,5,8,10)
print(sorted(arr))
print(sorted(arr,reverse=True))
print("\n")
