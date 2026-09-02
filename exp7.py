import numpy as np
# 1D array
a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)

import numpy as np
zeros_array = np.zeros((3, 3))
print(zeros_array)

import numpy as np
ones_array = np.ones((3, 2))
print(ones_array)

import numpy as np
range_array = np.arange(0, 10, 2)
print(range_array)

import numpy as np
linear_array = np.linspace(0, 1, 5)
print(linear_array)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])
print(b)

import numpy as np
random_array = np.random.rand(2, 3)
print(random_array)

arr1 = np.array([[4, 7], [2, 6]], dtype=np.float64)
arr2 = np.array([[3, 6], [2, 8]], dtype=np.float64)
print(arr1)
print(arr2)
print(np.add(arr1, arr2))
print(np.sum(arr1))
print(np.sqrt(arr1))
print(arr1.T)

import numpy as np
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x + y)
print(np.add(x, y))
print()
print(x - y)
print(np.subtract(x, y))
print()
print(x * y)
print(np.multiply(x, y))
print()
print(x / y)
print(np.divide(x, y))
print()
print(np.sqrt(x))

import numpy as np
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print(x)
print(y)
v = np.array([9,10])
w = np.array([11, 12])
print(v)
print(w)
# Inner product of vectors; both produce 219 (9×11)+(10×12)
print(v.dot(w))
print(np.dot(v, w))
print(np.multiply(v,w))

print(x.dot(v))
print(np.dot(x, v))

import numpy as np
array = np.array([1, 2, 3])
mean_value = np.mean(array)
print(mean_value)

import numpy as np
array = np.array([1, 2, 3])
print(array)
max_val = np.max(array)
min_val = np.min(array)
print(max_val)
print(min_val)

import numpy as np
array = np.array([1, 2, 3, 4])
element = array[2]
print(element)

import numpy as np
subset = array[1:3]
print(subset)

import numpy as np
array = np.array([1, 2])
indices = np.where(array > 2)
print(indices)