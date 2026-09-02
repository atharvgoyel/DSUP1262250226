def check_prime(num):
  if num ==1:
    print(" prime no")
  return
  if num==2 or num==3:
    print("prime no")
  return
  if num%2==0 or num%3==0:
    print("Not prime")
  return
  count=5
  for count in range(5,num,count+6):
    if (num % count) == 0 or ((num) % count+2==0):
      print("Not prime")
      return
print("prime no")

def calculate_factorial(num):
  fact = 1
  if num > 0:
    for count in range(1, num + 1):
      fact *= count
      print("\nFactorial of ", num, " is", fact)
  elif num == 0:
    print("\nFactorial of 0 is 1")
  else:
    print("\nPlease enter a non-negative integer !")

def add(a, b):
  result = a + b
  return result
def sub(a, b):
  result = a - b
  return result
def mul(a, b):
  result = a * b
  return result
def div(a, b):
  result = a / b
  return result

from module1 import check_prime
number = int(input("\nEnter number = "))
print(check_prime(number))
print(calculate_factorial(number))

import module2 as m1
a, b = map(int, input("Enter two numbers separated by a space: ").split())
print(m1.add(a,b))
print(m1.mul(a,b))

def check_prime(num):
  if num ==1:
    print(" prime no")
  return
  if num==2 or num==3:
    print("prime no")
  return
  if num%2==0 or num%3==0:
    print("Not prime")
  return
  count=5
  for count in range(5,num,count+6):
    if (num % count) == 0 or ((num) % count+2==0):
      print("Not prime")
  return
  print("prime no")

def calculate_factorial(num):
  fact = 1
  if num > 0:
    for count in range(1, num + 1):
      fact *= count
    print("\nFactorial of ", num, " is", fact)
  elif num == 0:
    print("\nFactorial of 0 is 1")
  else:
    print("\nPlease enter a non-negative integer !")

def add(a, b):
  result = a + b
  return result
def sub(a, b):
  result = a - b
  return result
def mul(a, b):
  result = a * b
  return result
def div(a, b):
  result = a / b
  return result

#import module1 as m
from module1 import check_prime
number = int(input("\nEnter number = "))
print(check_prime(number))
print(calculate_factorial(number))

import module2 as m1
a, b = map(int, input("Enter two numbers separated by a space: ").split())
print(m1.add(a,b))
print(m1.mul(a,b))

!mkdir my_package

# Commented out IPython magic to ensure Python compatibility.
# %%writefile my_package/module1.py
# def check_prime(num):
# if num ==1:
# print(" prime no")
# return
# if num==2 or num==3:
# print("prime no")
# return
# if num%2==0 or num%3==0:
# print("Not prime")
# return
# count=5
# for count in range(5,num,count+6):
# if (num % count) == 0 or ((num) % count+2==0):
# print("Not prime")
# return
# print("prime no")
# 
# def calculate_factorial(num):
# fact = 1
# if num > 0:
# for count in range(1, num + 1):
# fact *= count
# print("\nFactorial of ", num, " is", fact)
# elif num == 0:
# print("\nFactorial of 0 is 1")
# else:
# print("\nPlease enter a non-negative integer !")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile my_package/module2.py
# def add(a, b):
# result = a + b
# return result
# def sub(a, b):
# result = a - b
# return result
# def mul(a, b):
#   result = a * b
# return result
# def div(a, b):
# result = a / b
# return result

from my_package import module1 as m
number = int(input("\nEnter number = "))
print(m.check_prime(number))
print(m.calculate_factorial(number))

from my_package import module2 as m
a, b = map(int, input("Enter two numbers separated by a space: ").split())
print(m.add(a,b))
print(m.mul(a,b))

import math
print(math.sqrt(16))
# Import only the sqrt function from the math package
from math import sqrt
print(sqrt(25))

import numpy as np
a = np.arange(6)
a

a = np.array([2, 3, 4])
a

b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)

c = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=complex)
c

a = np.arange(15).reshape(3, 5)
a

a.shape

a.ndim

a.dtype.name

a.size

a = np.array([20, 30, 40, 50])
print(a)
b = np.arange(4)
print(b)
c=a-b
print(c)

a = np.array([[-1, 2, 0, 4],
[4, -0.5, 6, 0],
[2.6, 0, 7, 8],
[3, -7, 4, 2.0]])

a = a[:2, ::2]
print ("first 2 rows and alternate columns(0 and 2):\n", a)