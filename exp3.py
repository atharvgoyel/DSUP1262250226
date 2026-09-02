a=12
print(id(a))
b=a
print(id(b))
a=13
print(id(a))

a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types
print(a)
print(b)
print(c)

a = [10, 20, "GfG", 40, True]
print(a)
print(a[0])
print(a[1])
print(a[2])

a = list((1, 2, 3, 'apple', 4.5))
print(a)
b = list("MIT")
print(b)

# Creating List with Repeated Elements
a = [2] * 5
b = [0] * 7
print(a)
print(b)

a = [10, 20, 30, 40, 50]
print(a[0])
print(a[4])
print(a[-1])
print(a[1:4]) # elements from index 1 to 3

a = []
a.append(10)
print("After append(10):", a)
a.insert(0, 5)
print("After insert(1, 5):", a)
a.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)
a.clear()
print("After clear():", a)

#Appending Using a Loop
a = []
for i in range(5):
 a.append(i)
print(a)

#Python Insert List in Another List
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1=list1+list2
print(list1)

#Inserting a Tuple into the List
list1 = [ 1, 2, 3, 4, 5, 6 ]
# tuple of numbers
num_tuple = (4, 5, 6)
# inserting a tuple to the list
list1.insert(2, num_tuple)
print(list1)
print(list1[2][1])

#Inserting an Element at the end of the List
fruits = ['apple', 'banana', 'cherry']
fruits.insert(2, 'orange')
print(fruits)

#Insert elements of a set to a list in Python
list1 = [1, 2, 3]
s= {4,5,6}
list1.insert(3,s)
print(list1)

# Updating Elements into List
# Since lists are mutable, we can update elements by accessing them via their index.
a = [10, 20, 30, 40, 50]
a[1] = 25
print(a)

a = [10, 20, 30, 40, 50,30]
a.remove(30)
print("After remove(30):", a)

a = [10, 20, 30, 40, 50]
popped_val = a.pop()
print("Popped element:", popped_val)
print("After pop(1):", a)

a = [10, 20, 30, 40, 50]
del a[0]
print("After del a[0]:", a)

#Removing multiple elements by index range
a = [10, 20, 30, 40, 50, 60, 70]
del a[1:4]
print(a)

a = list()
b = list((1, 2, 3))
c = list("GfG")
print(a, type(a))
print(b, type(a))
print(c, type(a))

a = list(range(3))
print(a)
# Convert a comprehension to list
b = list(x * x for x in range(5))
print(b)

matrix = [ [1, 2, 3],
[4, 5, 6],
[7, 8, 9] ]
print(matrix[1])
print(matrix[1][2])

squares = [x**2 for x in range(1, 6)]
print(squares)

#Get the items from a list starting at position 1 and ending at position 4 (exclusive).
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements from index 1 to 4 (excluded)
print(a[1:4])

#Get all the items from a list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get all elements in the list
print(a[::])
print(a[:])

#Get all items before/after a specific position
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements starting from index 2
# to the end of the list
b = a[2:]
print(b)

# Get elements starting from index 0
# to index 3 (excluding 3th index)
c = a[:3]
print(c)

#Get items at specified intervals USE STEP PARAMETER
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get every second element from the list
# starting from the beginning
b = a[::2]
print(b)

# Get every third element from the list
# starting from index 1 to 8(exclusive)
c = a[1:8:3]
print(c)

# Negative Indexing
# Negative indexing is useful for accessing elements from the end of the list. The last
#element has an index of -1, the second last element -2, and so on.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[-2:]
print(b)

# Get elements starting from index 0
# to index -3 (excluding 3th last index)
c = a[0:6]
print(c)

# Get elements from index -4
# to -1 (excluding index -1)
a=[1,2,3,4,5,6,7,8,9]
d = a[-4:-1]
print(d)

# Get every 2nd elements from index -8
# to -1 (excluding index -1)
a=[1,2,3,4,5,6,7,8,9]
e = a[-8:-1:2]
print(e)

#Reverse a list using slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get the entire list using negative step
print(a[::-1])

t1 = (1, 2, 3, 4,5,6,7)
*a, b, c = t1
print(f"Original tuple: {t1}")
print(f"Unpacked variables: a={a}, b={b}, c={c}")

a = [1, 3, 5, 7, 9]
for i, x in enumerate(a):
 print(i, x)

a = [1, 3, 5, 7, 9]
i = 0
while i < len(a):
 print(a[i])
 i += 1

a = [1, 3, 5, 7, 9]
print(len(a))
print("\n")
for i in range(len(a)):
 print(a[i])

a = [1, 3, 5, 7, 9]
print(len(a))
print("\n")
for i in range(len(a)):
 print(a[i])

print("MIT", "WPU", "PUNE", sep="\n")

print("MIT " , end="")
print("WPU")

a = [1, 2, 3, 2]
# Count occurrences of 2 in the list
print(a.count(2))

a = [1, 2, 3]
# Reverse the list order
a.reverse()
print(a)

a = [3, 1, 2]
# Sort the list in ascending order
a.sort()
print(a)
#Sort the list in descending order
a.sort(reverse=True)
print(a)

# Find the maximum price in the list price
prices = [159.54, 37.13, 71.17]
price_max = max(prices)
print(price_max)

months = ['January', 'February', 'March']
prices = [238.11, 237.81, 238.91]
# Identify min price
min_price = min(prices)
print(min_price)
# Identify min price index
min_index = prices.index(min_price)
print(min_index)
# Identify the month with min price
min_month = months[min_index]
print(min_month)

empty_tuple = ()
print("Empty Tuple:", empty_tuple)
# Tuple with elements
numbers = (10, 20, 30, 40)
print("Numbers Tuple:", numbers)

# Mixed data tuple
mixed = (10, "Hello", 3.14, True)
print("Mixed Tuple:", mixed)
# Nested tuple
nested = (1, 2, (3, 4, 5))
print("Nested Tuple:", nested)

# Tuple without parentheses
implicit_tuple = 1, 2, 3, 4
print("Tuple without parentheses:", implicit_tuple)

# Single element tuple
single = (10,)
print(type(single))
print("Single Element Tuple:", single)
print()

# Concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2
print("Concatenated Tuple:", combined)

# Repetition
repeated = t1 * 2
print("Repeated Tuple:", repeated)

# Length
print("Length of tuple:", len(t1))
print()

# Indexing
colors = ("red", "green", "blue", "yellow", "purple")
print("First element:", colors[0])
print("Third element:", colors[2])
print("Last element:", colors[-1])

colors = ("red", "green", "blue", "yellow", "purple")
print("Colors[0:3]:", colors[0:3])
print("Colors[2:]:", colors[2:])
print("Colors[:4]:", colors[:4])
print("Colors[-3:]:", colors[-3:])
print()

nums = (15, 8, 22, 5, 13, 30)
print("Tuple:", nums)
print("Length:", len(nums))
print("Maximum:", max(nums))
print("Minimum:", min(nums))
print("Sum:", sum(nums))
print("Sorted (as list):", nums.sort())
t = (1, 2, 3, 4, 5)

# Convert tuple to list
tuple_data = (1, 2, 3, 4)
list_data = list(tuple_data)
print("Tuple to List:", list_data)

# Modify list
list_data.append(5)
print("Modified List:", list_data)

# Convert back to tuple
tuple_data = tuple(list_data)
print("List back to Tuple:", tuple_data)
print()