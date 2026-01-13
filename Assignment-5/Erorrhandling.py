#1 Write a program to handle division by zero error.

num1= int(input("Enter numerator: "))
num2= int(input("Enter denominator: "))
try:
    result= num1/num2
    print("Result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#2 Write a program to handle invalid integer input.
try:
    user_input = int(input("Enter an integer: "))
    
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")


#3 Write a program to open a file and handle the “file not found” error.

try :
    file =open("file.txt",'r')
except FileNotFoundError :
    print("error :file not open ")

#4  Write a program to demonstrate multiple exception blocks.

try :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result is:", result)
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#5 Write a program to use finally for resource cleanup.

try :
    file = open("sam.txt","r")
    conetent = file.read()
    print(conetent)
except FileNotFoundError :
    print("error :file not open ")
finally :
    file.close()
    print("file close successfully")

# 6 Write a program to create a custom exception for invalid age (<18).
class InvalidAgeError(Exception):
    pass
try :
    age = int(input("Enter your age: "))
    if age < 18 :
        raise InvalidAgeError("Age must be at least 18.")
    else :
        print("Valid age:", age)
except InvalidAgeError as e :
    print("Error:", e)


#7 Write a program to handle IndexError when accessing a list.

mylist=[10,20,30,40,50]
try :
    index = int(input("enter index number strating from 0:"))
    print("Element at index", index, "is:", mylist[index])
except IndexError :
    print("error :index out of range ")
    

#8 Write a program that takes two numbers and handles all possible errors.

try :
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result is:", result)
except ValueError :
    print("Error: Invalid input. Please enter valid numbers.")
except ZeroDivisionError :
    print("Error: Division by zero is not allowed.")

# Write a program to log errors to a file instead of printing them.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except Exception as e:
    with open("error.txt", "a") as file:
        file.write(str(e) + "\n")


#10  Write a program that validates an email format and raises an exception for invalid ones.	
class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format")

    print("Valid Email:", email)

except InvalidEmailError as e:
    print("Error:", e)
