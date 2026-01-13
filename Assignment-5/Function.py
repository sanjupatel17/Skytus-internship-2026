# 1Function to check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

if is_prime(n):
    print("Number is Prime")
else:
    print("Number is NOT Prime")

    
# 2Function to reverse a string.

def reverse_string(s):
    return s[ : : -1]
string  = input("Enter a string: ")
reversed_str = reverse_string(string)
print("Reversed string:", reversed_str)


# 3Function to find factorial.

def factorial(n):
    if n == 0 or n == 1:
        return 1

    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact


n= int(input("Enter a number: "))
print("Factorial =", factorial(n))





# 4Function to calculate simple interest.

def simple_interest(principal,rate,time):
    si=(principal*rate*time)/100
    return si 

p = int(input("Enter principal: "))
r = int(input("Enter rate: "))
t = int(input("Enter time (month): "))
print("Simple Interest =", simple_interest(p, r, t))

# 5Function to check if a word is palindrome.

def is_palindrome(word):
    return word == word[ : : -1]
word = input("Enter a word: ")
print("word is palindrome:",is_palindrome(word))

# 6Function to count vowels in a string.

def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in text:
        if ch in vowels:
            count += 1

    return count

string  = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))



# 7Function to merge two lists.

def merge_list(list1,list2):
    return list1 + list2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_list(list1, list2)
print("Merged List:", merged_list)


# 8Function to find GCD of two numbers.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD =", gcd(x, y))
    
# 9Function to find area of rectangle.

def area_of_rectangle(length, width):
    return length * width
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print("Area of rectangle =", area_of_rectangle(length, width))

# 10Function to check Armstrong number.
def is_armstrong(n):
    num_str=str(n)
    num_digits=len(num_str)
    sum = 0
    for digit in num_str:
        sum = sum + int(digit) ** num_digits

    return sum == n

num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
