
#Create a NumPy array:
#[[10, 20, 30],
# [40, 50, 60]]
import numpy as np

arr = np.array([[10, 20, 30],   [40, 50, 60]])

print("Array:")
print(arr)

print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Data Type:", arr.dtype)


#2. Reshape an array into 2 × 4 matrix and convert back using ravel()
#[1, 2, 3, 4, 5, 6, 7, 8]
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

matrix = arr.reshape(2, 4)

print("2D Matrix:")
print(matrix)

new_arr = matrix.ravel()

print("1D Array:")
print(new_arr)


# 3. Find sum, cumulative sum, and product
# [5, 10, 15, 20, 25]
import numpy as np

arr = np.array([5, 10, 15, 20, 25])

print("Sum:", np.sum(arr))

print("Cumulative Sum:", np.cumsum(arr))

print("Product:", np.prod(arr))


# 4. Find maximum, index of maximum and clip values
# [12, 45, 22, 78, 34]
import numpy as np

arr = np.array([12, 45, 22, 78, 34])

print("Maximum:", np.max(arr))

print("Index of Maximum:", np.argmax(arr))

print("Clipped Array:", np.clip(arr, 20, 50))


# 5. Split the array into 3 equal parts using np.split()
# [1, 2, 3, 4, 5, 6]
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

result = np.split(arr, 3)

print(result)


# 6. Concatenate, stack vertically and stack horizontally
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Concatenate:")
print(np.concatenate((a, b)))

print("Vertical Stack:")
print(np.vstack((a, b)))

print("Horizontal Stack:")
print(np.hstack((a, b)))