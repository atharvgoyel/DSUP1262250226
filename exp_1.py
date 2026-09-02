print("Hello")

a,b = map(int, input("Enter value for a and b: ").split())
print("Sum =", a+b)

x = 5
y = 3.14
z = "Hi"
print(x,y,z)

x = 10
print(type(x))
x = "Now a string"
print(type(x))

a = b = c = 100
print(a, b, c)
x, y, z = 1, 2.5, "Python"
print(x, y, z)

a=10
print(id(a))
b=a
print(id(b))
a= 20
print(id(a))

x = 10
del x
print(x)

a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

a = True
b = False
print(a and b)
print(a or b)
print(not a)

#Bitwise Operators
a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
0

#Assignment Operators
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

#Identity Operators
a = 10
b = 20
c = a
print(a is not b)
print(a is c)

#Membership Operators
x = 24
y = 20
my_list = [10, 20, 30, 40, 50]
if (x not in my_list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
if (y in my_list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

#Ternary Operators
a, b = 10, 20
if a<b:
 print(min)

import keyword
print("The list of keywords are : ")
print(keyword.kwlist)

#Numeric Data Type
a = 5
b = 5.0
c = 2 + 4j
print(type(a))
print(type(b))
print(type(c))

#Sequence Data Type---> String
s = 'Welcome to the Geeks World'
print(s)
print(type(s))
# access string with index
print(s[1])
print(s[-1])

#Sequence Data Type---> List
a = [1, 2, 3]
print(a)
b = ["Geeks", "For", "Geeks", 4, 5]
print(b[3])
print(b[-3])

#Sequence Data Type---> Tuple
t1 = (1,)
print(type(t1))
t2 = ('Geeks', 'For', 'Geeks', 1, 2)
print(t2[3])
print(t2[-3])

#Boolean Data Type
print(type(True))
print(type(False))

#Set Data Type
s1 = {"a", "a", "b", "c", "b"}
print(s1)
s2 = {"Geeks", "For", "Geeks"}
for i in s2:
 print(i)

#Dictionary Data Type
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d[1])
print(d.get(2))

number = int(input('Enter a number: '))
# check if number is greater than 0
if number > 0:
    print('number is a positive number.')
else:
    print('number is a negative number.')

number = -5
if number > 0:
 print('Positive number')
elif number < 0:
 print('Negative number')
else:
 print('Zero')
print('This statement is always executed')

score = int(input("Enter the student's score: "))
if score >= 90:
 print("Grade: A")
elif score >= 80:
 print("Grade: B")
elif score >= 70:
 print("Grade: C")
elif score >= 60:
 print("Grade: D")
else:
 print("Grade: F")

a, b = 10, 20
if a < 50:
    if b < 100:
        print("a is less than 50 and b is less than 100")
    else:
        print("a is less than 50 but b is not less than 100")
else:
    print("a is not less than 50")

# Largest of 3 numbers
num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is", largest)

#Check number is Positive or Negative
num = int(input("Enter a number: "))
if num > 0:
 print("Positive number")
elif num == 0:
 print("Zero")
else:
 print("Negative number")

#Odd or Even
num = int(input("Enter a number: "))
if (num % 2) == 0:
 print("{0} is Even".format(num))
else:
 print("{0} is Odd".format(num))

# iterate from i = 0 to i = 3
for i in range(0, 4):
 print(i)

# iterate from i = 0 to i = 3
for i in range(1, 4):
 print(i)

# iterate from i = 0 to i = 3
for i in range(0, 10,2):
 print(i)

# iterate from i = 0 to i = 3
for i in range(1, 10,2):
 print(i)

n = int(input("Enter a number"))
for i in range(0, n):
 print(i)

list1 = ['MIT', 'WPU', 'Pune']
for i in list1:
 print(i)

list1 = ['MIT', 'WPU', 'Pune']
for i in list1:
    if i == 'Pune':
        break
    print(i)

list1 = ['MIT', 'WPU', 'Pune','India']
for i in list1:
    if i == 'Pune':
        continue
    print(i)

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
   if i == 3:
     continue
   print(i)

n = 10
# use pass inside if statement
if n > 10:
 pass
print('Hello')

x = 10
if x > 5:
 pass# Code will be added later
else:
 print("x is 5 or less")