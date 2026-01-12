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

