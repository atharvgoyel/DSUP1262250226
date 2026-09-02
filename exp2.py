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
    pass  # Code will be added later
else:
    print("x is 5 or less")

# 1. Basic For Loop
# Iterate through a list of numbers and print them.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# 2. Sum of Elements in a List
# Using a loop to find the total of all elements.
arr = [10, 20, 30, 40, 50]
total = 0
for val in arr:
    total += val
print("Sum =", total)

# 3. Find Maximum Element (Array Traversal - DSA)
arr = [12, 45, 23, 51, 19, 8]
max_val = arr[0]
for num in arr:
    if num > max_val:
        max_val = num

print("Maximum Element:", max_val)

# 4. Loop Through a Dictionary
# Useful for problems involving key-value pairs (maps).
student = {"name": "Mrunal", "age": 21, "marks": 92}
for key, value in student.items():
    print(key, ":", value)

# 5. Reverse a String (Common DSA Task)
string = "Python"
reversed_str = ""
for ch in string:
    reversed_str = ch + reversed_str
print("Reversed:", reversed_str)

# 6. Counting Frequency of Elements (DSA Hash Map Use)
arr = [1, 2, 2, 3, 1, 4, 2]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print(freq)

# 7. Linear Search (Fundamental DSA Algorithm)
arr = [4, 7, 1, 9, 3]
key = 9
found = False
for val in arr:
    if val == key:
        found = True
        break

print("Element Found!" if found else "Not Found")

# 8. Factorial Using For Loop
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "is", fact)

# 9. Fibonacci Series (Iterative DSA Example)
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

num = 10
if num > 0:
    print("Positive number")

# if-else Statement
# Executes one block if true, another if false.
num = -5
if num >= 0:
    print("Positive number")
else:
    print("Negative number")

# if-elif-else Ladder
# Used when there are multiple conditions to check.
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")

# Nested if-else Example
# An if statement inside another if or else block.
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is zero or negative")

# DSA-Style Example: Find Largest of Three Numbers
# Demonstrates nested conditional logic — similar to comparison logic in algorithms.
a, b, c = 10, 25, 15
if a > b:
    if a > c:
        print("Largest:", a)
    else:
        print("Largest:", c)
else:
    if b > c:
        print("Largest:", b)
    else:
        print("Largest:", c)

# Even-Odd and Divisibility Check
# Combination of if-elif-else and nesting.
num = 30

if num % 2 == 0:
    if num % 5 == 0:
        print("Even and divisible by 5")
    else:
        print("Even but not divisible by 5")
else:
    print("Odd number")

# DSA Concept Example - Search Result
# A conditional check while traversing a list.

arr = [3, 8, 1, 9, 5]
key = 9

found = False
for val in arr:
    if val == key:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")

#Nested Loop Example
for i in range(1, 4): # Outer loop for rows
 for j in range(1, 4): # Inner loop for columns
  print(j, end=" ")
print() # Move to next line after inner loop

#Right-Angled Triangle Pattern
# Program 1: Right-Angled Triangle
for i in range(1, 6):
 for j in range(1, i + 1):
  print("*", end=" ")
print()

#Inverted Right-Angled Triangle
# Program 2: Inverted Triangle

for i in range(5, 0, -1):
 for j in range(1, i + 1):
  print("*", end=" ")
print()

#Number Triangle Pattern
# Program 3: Number Pattern
for i in range(1, 6):
 for j in range(1, i + 1):
  print(j, end=" ")
print()

#Pyramid Pattern
# Program 4: Pyramid Pattern
rows = 5
for i in range(1, rows + 1):
 print(" " * (rows - i), end="") # Spaces
print("* " * i)

#Alphabet Pattern
# Program 6: Alphabet Triangle
ch = 65 # ASCII for 'A'
for i in range(5):
 for j in range(i + 1):
  print(chr(ch), end=" ")
ch += 1
print()

#Floyd’s Triangle (Number Sequence)
# Program 7: Floyd's Triangle
num = 1
for i in range(1, 6):
 for j in range(1, i + 1):
  print(num, end=" ")
num += 1
print()

#Diamond Pattern
# Program 8: Diamond Pattern
rows = 5
# Upper part
for i in range(1, rows + 1):
 print(" " * (rows - i) + "* " * i)
# Lower part
for i in range(rows - 1, 0, -1):
 print(" " * (rows - i) + "* " * i)

#Continue Statement Example
for num in range(1, 11):
 if num % 3 == 0:
  continue # Skip multiples of 3
print(num)

#Pass Statement Example

for letter in "PYTHON":
 if letter == "H":
  pass # Placeholder — no action for 'H'
print("Pass block executed for letter:", letter)
print("Current letter:", letter)