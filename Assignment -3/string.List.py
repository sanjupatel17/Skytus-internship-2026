# 1 Take a string input and print its length.


string= "My name is sanju "
print(len(string))

# 2 Convert a sentence to lowercase.

string= "My NAME IS SANJU "
print(string.lower())

# 3 Replace spaces with underscores in a string.

text = "Tommorow is working day"
modified_text=text.replace(" ","_")
print(modified_text)


# 4 Extract the first and last character of a string.

string = "sanjay"
print(string[0])
print(string[-1])

# 5 Reverse a string using slicing.

string = "sanjay"
reversed_string=string[::-1]
print(reversed_string)

# 6 Count how many times a letter appears in a string.


lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
letter = "a"
count=lorem.count(letter)
print(f"In sentence {letter} is appered {count}")


# 7 Check if a word is present in a sentence.

str = "Dummy text sections filled with fun lorem ipsum make it easier to swap out one web page"
word = "ipsum"
if word in str:
    print("word is present str")
else:
    print("word is not present in str")
 
# 8 Take name & age and print using f-string formatting.

name = input("Enter your name:")
Age = input("Enter your Age:")
print(f"your name is {name} and you are {Age} old.")


# 9 Remove extra spaces from the start and end of a string.

str = "  removal whitespace  "
print(str.strip())


# 10 Join a list of words into a single string with - between them.

myTuple = ("John", "Peter", "Vicky")
x = "-".join(myTuple)
print(x)


# 11 Create a list of your 5 favorite movies.

mylist = ["apple", "banana", "cherry", "Mango" , "watermelon"]
print(mylist)


# 12 Add a new movie to the list.

mylist = ["apple", "banana", "cherry", "Mango" , "watermelon"]
mylist.append("orange")
print(mylist)

# 13 Remove the first movie from the list.


mylist = ["KGF", "KRISH", "KGF2", "TOXIC" , "AVATAR"]
mylist.pop(0)  #mylist.remove(KGF)
print(mylist)

# 14 Sort a list of numbers in ascending order.

mylist = [1,2,5,7,9,35]
mylist.sort()
print(mylist)

# 15 Reverse a list.

mylist = [1,2,5,7,9,35]
mylist.reverse()
print(mylist)

# 16 Find the largest number in a list.

mylist = [1,2,5,7,9,35]
print("Max number in mylist is",max(mylist))

# 17 Merge two lists into one.


mylist = [1,2,5,7,9,35]
mylist2 = [1, 2, 3]

print("Merged two list is",mylist + mylist2)
    
# 18 Access the last element of a list without using index number.

mylist = [1,2,5,7,9,35]
last_element=mylist.pop()
print(last_element)

# 19 Create a nested list and access a specific inner element.

nested_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
element = nested_list[1][1]

print("Nested List:", nested_list)
print("Accessed Element:", element)

 
# 20 Count how many times an element appears in a list.

numbers = [10, 20, 30, 20, 40, 20, 50]
element = 20
count = numbers.count(element)
print("element count is 20")
print("count:",count)

 
