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