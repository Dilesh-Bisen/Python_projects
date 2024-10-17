# 1. union() : The union() methods prints all items that are present in the two sets. The union() method returns a new set.
print("\nunion() method : ")
a1 = {1, 2, 3, 4, 5}
b1 = {5, 6, 7, 8, 9}
c = a1.union(b1)
print(c)
print("a1 :", a1, "\nb1 :", b1)


# 2. update() : The update() methods prints all items that are present in the two sets.The update() method adds item into the existing set from another set.
print("\nupdate() method : ")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.update(cities2)
print("cities1 : ", cities1, "\ncities2 : ", cities2)


# 3. intersection() : The intersection() methods prints only items that are similar to both the sets. The intersection() method returns a new set.
print("\nintersection() method : ")
a2 = {1, 2, 3, 4, 7, 9, }
b2 = {5, 6, 7, 8, 9, 1}
c = a2.intersection(b2)
print(c)
print("a2 :", a2, "\nb2 :", b2)


# 4. intersection_update() : The intersection() methods prints only items that are similar to both the sets.A intersection_update() method updates into the existing set from another set.
print("\nintersection_update() method : ")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.intersection_update(cities2)
print("cities1 : ", cities1, "\ncities2 : ", cities2)


# 5. symmetric_difference() : The symmetric_difference() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set.
print("\nsymmetric_difference() method : ")
a3 = {1, 2, 3, 4, 5, 6}
b3 = {5, 6, 7, 8, 9}
c3 = a3.symmetric_difference(b3)
print(c3)
print("a3 :", a3, "\nb3 :", b3)


# 6. symmetric_difference_update() : This methods prints only items that are not similar to both the sets. The symmetric_difference_update() method updates into the existing set from another set.
print("\nsymmetric_difference_update() method : ")
a4 = {1, 2, 3, 4, 5, 6}
b4 = {5, 6, 7, 8, 9}
a4.symmetric_difference_update(b4)
print("a4 : ", a4, "\nb4 : ", b4)


# 7. difference() : The difference() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set.
print("\ndifference() method : ")
a5 = {1, 2, 3, 4, 5, 6}
b5 = {5, 6, 7, 8, 9}
c5 = a5.difference(b5)
print(c5)
print("a5 : ", a5, "\nb5 : ", b5)


# 8. difference_update() : The difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference_update() method updates into the existing set from another set.
print("\ndifference_update() method : ")
a6 = {1, 2, 3, 4, 5, 6}
b6 = {5, 6, 7, 8, 9}
a6.difference_update(b6)
print("a6 : ", a6, "\nb6 : ", b6)


# 9. isdisjoint() : The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
print("\nisdisjoint() method : ")
a7 = {1, 2, 3, 4, 5, 6}
b7 = {5, 6, 7, 8, 9}
print(a7.isdisjoint(b7))
a7 = {1, 2, 3, 4}
b7 = {5, 6, 7, 8, 9}
print(a7.isdisjoint(b7))


# 10. issuperset() : The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
print("\nissuperset() method : ")
d = {1, 2, 3, 4, 5, 6}
e = {5, 6, 7, 8, 9}
print(d.issuperset(e))
i = {1, 2, 3, 4, 5, 6, 7, 8, 9}
j = {5, 6, 7, 8, 9}
print(i.issuperset(j))


# 11. issubset() : The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
print("\nissubset() method : ")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))


# add() : If you want to add a single item to the set use the add() method.
print("\nadd() method : ")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Dilesh")
print(cities)


# remove()/discard() : We can use remove() and discard() methods to remove items form list.
# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.
print("\nremove() method : ")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Dilesh")  # provide an error
cities.discard("Dilesh")  # no error
print(cities)


# pop() : This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
print("\npop() method : ")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print("pop item : ", item)
print("Set elements is changed : ", cities)


# del : del is not a method, rather it is a keyword which deletes the set entirely.NameError: name 'cities' is not defined We get an error because our entire set has been deleted and there is no variable called cities which contains a set.
print("\ndel : ")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)


# clear() : This method clears all items in the set and prints an empty set.
# What if we don’t want to delete the entire set, we just want to delete all items within that set?
print("\nclear : ")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print("Empty set : ", cities)


print("\nCheck if item exists : ")
info = {"Dilesh", 19, False, 5.9}
if "Dilesh" in info:
    print("Dilesh is present.")
else:
    print("Dilesh is absent.")


