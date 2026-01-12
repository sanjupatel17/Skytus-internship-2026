
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
fruits = {"apple", "banana", "cherry", "Mango","Kiwi"}
fruits.add("orange")
print(fruits)




# 26 Remove an element from a set.
fruits = {"apple", "banana", "cherry", "Mango","Kiwi"}
fruits.remove("banana")
print(fruits)


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


#DICTONARY OPERATIONS


# 31 Create a dictionary storing student names and marks.

student_dict = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92, "Eve": 88}
print(student_dict)

#32 Add a new key-value pair to an existing dictionary.

student_dict["Frank"] = 95
print(student_dict)

# 33 Delete a key-value pair from a dictionary.

student_dict = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92, "Eve": 88}
del student_dict["Alice"]
print(student_dict)



# 34 Merge two dictionaries into one.


student_dict = {"Meet": 85, "Bob": 90, "Nij": 78, "Diana": 92, "sanju": 88}
student_dict2 = {"man": 95, "sam": 89}
student_dict.update(student_dict2)
print(student_dict)


#35 Check if a key exists in a dictionary.

student_dict = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92, "Eve": 88}
key_to_check="Bob"

if key_to_check in student_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")

#36 Count word frequency in a given string using a dictionarytext.split().


text="hello my name is sanju and my friend name is sanjay"
word_list = text.split()
word_freq={}
for word in word_list:
    if word in word_freq :
        word_freq[word] += 1
    else :
        word_freq[word] =1
print(word_freq)  


#37 Find the key with the maximum value in a dictionary.

student_dict = {"Meet": 85, "Bob": 90, "Nij": 78, "Diana": 92, "sanju": 88}
max_key = max(student_dict,key=student_dict.get)
print(f"Key with maximum value is: {max_key} with value {student_dict[max_key]}")



#38 Reverse keys and values in a dictionary.

student_dict = {"Meet": 85, "Bob": 90, "Nij": 78, "Diana": 92, "sanju": 88}
reversed_dict = {value: key for key, value in student_dict.items()}
print(reversed_dict)



#39 Update the value for a specific key.

student_dict = {"Meet": 85, "Bob": 90, "Nij": 78, "Diana": 92, "sanju": 88}
student_dict["Meet"] = 95
print(student_dict)

#40 Convert a list of tuples into a dictionary.

tuple_list = [("Meet", 85), ("Bob", 90), ("Nij", 78), ("Diana", 92), ("sanju", 88)]
dict_from_tuples = dict(tuple_list)
print(dict_from_tuples)