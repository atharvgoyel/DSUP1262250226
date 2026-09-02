a = 25
b = 12.5
c = "Python"
d = True
print("Value:", a, "Type:", type(a))
print("Value:", b, "Type:", type(b))
print("Value:", c, "Type:", type(c))
print("Value:", d, "Type:", type(d))

a = "25"
b = "12.5"
c = 100
x = int(a)
y = float(b)
z = str(c)
print("Integer:", x, type(x))
print("Float:", y, type(y))
print("String:", z, type(z))
print("Boolean:", bool(c))

a = 10
b = 5.5
c = a + b
print("Implicit Conversion:")
print("Result:", c)
print("Type:", type(c))

x = "20"
y = int(x)
print("\nExplicit Conversion:")
print("Value:", y)
print("Type:", type(y))

num1 = int(input("Enter first integer: "))
num2 = float(input("Enter second number: "))

print("First number:", num1)
print("Type:", type(num1))
print("Second number:", num2)
print("Type:", type(num2))
print("Sum:", num1 + num2)

a = -25
b = 4.5678
numbers = [10, 25, 5, 40, 15]
print("Absolute value:", abs(a))
print("Power:", pow(2, 3))
print("Rounded value:", round(b, 2))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

marks = [75, 82, 68, 91, 85]
total = sum(marks)
count = len(marks)
highest = max(marks)
lowest = min(marks)
average = total / count
print("Marks:", marks)
print("Total:", total)
print("Number of Subjects:", count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

print("Average:", average)

import math
n = 25
print("Square Root:", math.sqrt(n))
print("Power:", math.pow(2, 3))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("Factorial:", math.factorial(5))
print("GCD:", math.gcd(24, 36))
print("Value of Pi:", math.pi)

def display():
  print("MIT World Peace University")
display()
display()

def addition(a, b):
  result = a + b
  print("Addition:", result)
addition(10, 20)
addition(25, 15)

def student(name, roll_no):
  print("Name:", name)
  print("Roll No:", roll_no)
student(roll_no=102, name="Amit")

def greet(name, message="Welcome to Python"):
  print(name, "-", message)
greet("Rahul")
greet("Amit", "Good Morning")

def addition(a, b):
  result = a + b
  return result
answer = addition(25, 15)
print("Result:", answer)

def calculate(a, b):
  total = a + b
  difference = a - b
  product = a * b
  return total, difference, product
x, y, z = calculate(20, 10)
print("Total:", x)
print("Difference:", y)
print("Product:", z)

x = 100
def display():
  print("Value of x inside function:", x)
display()
print("Value of x outside function:", x)

x = 100
def display():
  x = 50
  print("Inside function:", x)
display()
print("Outside function:", x)

x = 10
def update():
  global x
  x = 50
print("Before function call:", x)
update()
print("After function call:", x)

def calculate_result(m1, m2, m3):
  total = m1 + m2 + m3
  percentage = total / 3
  return total, percentage
m1 = int(input("Enter Python marks: "))
m2 = int(input("Enter Data Structure marks: "))
m3 = int(input("Enter Database marks: "))
total, percentage = calculate_result(m1, m2, m3)
print("Total Marks:", total)
print("Percentage:", percentage)

def largest(a, b, c):
  return max(a, b, c)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
result = largest(x, y, z)
print("Largest Number:", result)