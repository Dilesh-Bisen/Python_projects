# def gen(n):
#     for i in range(n):
#         yield i


# # print(gen(100))

# # for i in gen(100):
# #     print(i)


# ob1 = gen(100)
# print()


# a = [10, 20, "Python"]
# iter_obj = iter(a)

# while 1:
#     try:
#         item = next(iter_obj)
#         print(item)
#     except StopIteration:
#         break

print("\nuse of yield (generator function) :")
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]       # output is o l l e h
for i in rev_str("Hello"):
    print(i, end=" ")

print("\nuse of return (normal function) :")
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        return my_str[i]     # output is o
for i in rev_str("Hello"):
    print(i, end=" ")
