#1 Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.
class car :
    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self,increase):
        self.speed += increase 
        print(f"Car accelerated. Current speed: {self.speed} km/h")
  

    def brake(self,decrease):
        self.speed -= decrease
        print(f"Car decelerated. Current speed: {self.speed} km/h")


my_car = car("Toyota", "Corolla", 50)
my_car.accelerate(20)
my_car.brake(15)

#2 Create a BankAccount class with deposit and withdraw methods.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount}")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient funds")
        print(f"Current Balance: ₹{self.balance}")


my_account = BankAccount("2379479129", 1000)
my_account.deposit(500)
my_account.withdraw(1500)



# 3 Create a Student class with a method to calculate average marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        return avg


my_student = Student("Sanjay", [90, 67, 89, 98, 79, 69])

print("Student Name:", my_student.name)
print("Average marks:", my_student.average())



#4 Create a Rectangle class with methods to find area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(5,10)
print("Length:", my_rectangle.length)
print("Width:", my_rectangle.width)
print("Area",my_rectangle.area())
print("Perimeter:", my_rectangle.perimeter())



#5 Create an Employee class that displays salary details.
class Employee :
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_details(self):
        print(f"Employee Name:",self.name)
        print(f"Position:",self.position)
        print(f"Salary: {self.salary}")

my_employee = Employee("Sanjay","Software Engineer",50000)
my_employee.display_details()

#6 Create a Book class to store title, author, and price, and display details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

my_book = Book("Belive", "George Orwell", 15.99)
my_book.display_details()

#7 Create a Circle class to find area and circumference.

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius**2)

    def circumference(self):
        return 2*math.pi*self.radius
my_circle = Circle(9)
print("Radius:", my_circle.radius)
print("Area:", my_circle.area())
print("Circumference:", my_circle.circumference())


 
#8 Create a Laptop class with a method to apply discounts on price.

class Laptop :
    def __init__(self, brand, model, price):
        self.brand = brand 
        self.model = model
        self.price = price 
    def disscount(self,percentage):
        discount_amount = (percentage/100)*self.price
        return self.price - discount_amount
my_laptop = Laptop("Dell","XPS Series",120000)
print("Brand:", my_laptop.brand)
print("Model:", my_laptop.model)
print("Price after discount:", my_laptop.disscount(10))


#9 Create a Flight class with seat booking functionality.
class Flight:
    def __init__(self, flight_number, economy, business, first_class):
        self.flight_number = flight_number
        self.seats = {
            "economy": economy,
            "business": business,
            "first": first_class
        }
        self.booked = {
            "economy": 0,
            "business": 0,
            "first": 0
        }

    def book_seat(self, seat_class, seats):
        if seat_class not in self.seats:
            print("Invalid seat class")
            return

        if self.booked[seat_class] + seats <= self.seats[seat_class]:
            self.booked[seat_class] += seats
            print(f"{seats} {seat_class} seats booked successfully.")
        else:
            print(f"Not enough {seat_class} seats available.")

    def available_seats(self, seat_class):
        return self.seats[seat_class] - self.booked[seat_class]


flight1 = Flight("AI-202", economy=120, business=40, first_class=20)

flight1.book_seat("economy", 50)
flight1.book_seat("business", 20)
flight1.book_seat("first", 10)
flight1.book_seat("first", 15)

print("Available Economy seats:", flight1.available_seats("economy"))
print("Available Business seats:", flight1.available_seats("business"))
print("Available First Class seats:", flight1.available_seats("first"))

#10 Create a Shop class with a method to add and list products.

class Shop:
    def __init__(self, name,):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product)
my_shop = Shop("Tech Store")
my_shop.add_product("Laptop")
my_shop.add_product("Smartphone")
my_shop.add_product("Tablet")
my_shop.list_products()


            