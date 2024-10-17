a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

print("\nMerging a and b :\n", tuple(x))
print("Type of x :", type(tuple(x)))

print(list(zip()))
print(tuple(zip()))
print(dict(zip()))

l1 = [x for x in range(9)]
l2 = [chr(65+x) for x in range(12)]

for i, j in zip(l1, l2):
    print(i, j, sep=" : ")

d1 = dict(zip(l1, l2))
d2 = dict(zip(l2, l1))

print(d1.keys())
print(d2.keys())

print("\nlist as argument :")
for i, j in zip(l1, l2):
    print(i, j)

print("\ndictionary as argument :")
for i, j in zip(d1.keys(), d2.keys()):
    print(i, j)

print("\n")
for k, v in d1.items():
    print(k, v, sep=" : ", end="\t")


print("\n")
for (k1, v1), (k2, v2) in zip(d1.items(), d2.items()):
    print(k1, v1, k2, v2, sep=" : ")
