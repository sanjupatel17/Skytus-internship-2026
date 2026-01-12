
# 21 Create a tuple with 5 numbers.

tuple = ("apple", "banana", "cherry")
print(tuple)

# 22 Access the third element in a tuple.

tuple = ("apple", "banana", "cherry")
print(tuple[1])

# 23 Unpack a tuple into separate variables.

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# 24 Create a set of 5 fruits.

fruits = ("apple", "banana", "cherry", "Mango","Kiwi")
print(fruits)

# 25 Add a new fruit to the set.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(tuple(y))


# 26 Remove an element from a set.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(tuple(y))

# 27 Find union of two sets.


set1 = {1,2,3,4,5,7}
set2= {12.13,13,14,67}

union_set = set1.union(set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("the unio of two set is:",union_set)


# 28 Find intersection of two sets.

set1 = {1,2,3,4,5,7}
set2= {12,13,2,14,67}

intersection_set = set1.intersection(set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection of sets:", intersection_set)


# 29 Check if one set is subset of another.

set1 = {1,2,3,4,5,7}
set2= {1,2,3,5,4,6}

is_subset = set1.issubset(set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("subset  of sets:", is_subset)

# 30 Convert a list with duplicate values into a set to remove duplicates.

list = [1,2,34,21,34,56,56,7,8,79,9,21,79]
set_list=set(list)
print(set_list)