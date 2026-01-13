#1  Print numbers from 1 to 10.

for i in range(1,11):
    print(i)

# 2 Display multiplication table for a given number.

num = int(input("Enter the number which you want multiplication table for: "))
for i in range(1,11):
    print(f"{num} x {i}  = {i*num}")

#3 Find factorial of a number.

n = int(input("Enter a number to find its factorial:"))
factorial =1 
if n == 0 :
    print("Factorial of 0 is 1")
else :
    for i in range(1,n+1):
        factorial = factorial *i
        print(f"factoral is {n} is {factorial}")
         
# 4 Generate the first N Fibonacci numbers.

n = int(input("Enter a number to find its fibonaci series :"))
n1 = 0 
n2= 1
count = 0 
if n == 0 :
    print("Fibonacci of  0  is 0")
elif n == 1:
        print("Fibonacci of  1  is 1")
else :
    print(n1)
    print(n2)
    for i in range(2,n+1):
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3
        count += 1
                

# 5 Check if a number is prime.

n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Number is NOT prime")
            break
    else:
        print("Number is prime")
else:
    print("Number is NOT prime")


# 6 Reverse a number (e.g., 123 → 321).

n = input("Enter a number: ")
rev = ""

for i in n:
    rev = i + rev

print("Reversed number:", rev)


# 7 Count digits in a number.

n = (input("Enter a number :"))
count = 0 
for i in n:
    count += 1
    
print("Number of digits  is count: ",count)

#8 Find sum of even numbers between 1–100.

sum = 0
for i in range(1,101,2):
    
    sum = sum + i
print("sum of number is :",sum)

#9  Print a pyramid pattern.

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)


#10 Find all divisors of a number.

n = int(input("Enter a number: "))
print("Divisors of", n, "are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)