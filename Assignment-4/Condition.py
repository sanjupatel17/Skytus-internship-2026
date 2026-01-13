# 1 Check if a person is eligible to vote (age ≥ 18).

Age = int(input("Enter your age:"))
if Age >=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



#2 Grade calculator based on marks: 90+ = A, 80+ = B, else C.

marks = int(input("Enter your marks :"))
if marks >=90 :
    print("Grade A")
elif marks >=80 :
    print("Grade B")
else:
    print("Grade C")

#3 Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.

Light = input(("Enter the traffic light color (Red/Yellow/Green):")).lower()
if Light =="red":
    print("Stop")
elif Light =="yellow":
    print("Wait")
elif Light =="green":
    print("Go")
else:
   print("Invalid color")

#4 ATM withdrawal check: sufficient balance or not.
Amount = float(input("Enter withdrawal amount:"))
balance = 100000.0
if Amount <= balance:
    print("Sufficient balanace.")
else:
    print("Insufficient balance.")
   
#5 Check if a number is positive, negative, or zero.

num = float(input("Enter a number:"))
if num > 0:
    print("Positive number.")
elif num < 0:
    print("Negative number.")
else:
    print("Zero.")

#6 Check if a number lies within a given range.

lower = int(input("Enter lower bound of range:"))
upper = int(input("Enter upper bound of range:"))
num = float(input("Enter a number:"))
if lower <= num <= upper:
    print("Number lies within the range.")
else:
    print("Number does not lie within the range.")

#7 Username & password verification.

username = input("Enter username:")
password = input("Enter password:")
if username == "sanjubaba" and password == "sanju123":
    print("Access granted.")
else:
    print("Access denied.")



#8 Electricity bill calculator based on units consumed.

current_units = int(input("Enter units consumed:"))
previous_reading = int(input("Enter previous meter reading:"))
units_consumed = current_units - previous_reading
if units_consumed <= 100:
    bill_amount = units_consumed * 12.5
elif units_consumed <= 200:
    bill_amount = (100 * 12.5) + (units_consumed - 100) * 15
else:
    bill_amount = (100 * 12.5) + (100 * 15) + (units_consumed - 200) * 20
print("Total bill amount: Rs.", bill_amount)


#9 Simple calculator (add, subtract, multiply, divide).

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operation = input("Enter operation (+, -, *, /):")
if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero.")
else:
    print("Invalid operation.")
    
#10  Check type of triangle (equilateral, isosceles, scalene).
x = float(input("Enter length of first side:"))
y = float(input("Enter length of second side:"))
z = float(input("Enter length of third side:"))
if x==y==z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
