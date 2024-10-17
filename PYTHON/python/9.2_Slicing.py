# String Slicing : A string in Python can be sliced for getting a part of the string

a = "Dilesh"
print("Length of Dilesh is :", len(a))
#  D   i   l   e   s   h
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

# a[x : y]   ---> x(including) and y(excluding)

print("\n+ve index")
print("Slice string : ", a[2:])  # here 5 included
print("Slice string : ", a[1:3])
print("Slice string : ", a[:6])  # same as a[start(0)  : last element]
print("Slice string : ", a[0:])  # same as a[start(0)  : last element]
print("Slice string : ", a[:])  # same as a[start(0)  : last element]

print("\n-ve index")
print("Slice string : ", a[-6:-4])  # here -4 excluded
# It is same as  a[len(a) - 6 : len(a) - 4]
# start = -1 and stop = -len(a) and skip = 0
print("Slice string : ", a[::-1])
print("Slice string : ", a[-4:-6])  # nothing will print
print("Slice string : ", a[-4:-6:-1])  # now it will print
print("Slice string : ", a[:-2])  # same as a[start(-6) : -2]
print("Slice string : ", a[-6:])  # same as a[start(-6) : last element]


print("\nSlicing with the skip value :")

# a[x : y : z]     ----> x(including) , y(excluding) , z(z-1 character are skipped)
#  slice step cannot be zero(z! = 0) And z = 1 doesn`t skip the character

print("Slice string : ", a[0:6:2])
print("Slice string : ", a[::4])
