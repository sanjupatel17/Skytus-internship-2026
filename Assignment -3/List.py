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

 
