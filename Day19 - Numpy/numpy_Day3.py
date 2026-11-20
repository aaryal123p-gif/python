import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(numbers)
print("Total:", np.sum(numbers))
print("Average:", np.mean(numbers))

#np.where
where_result = np.where(numbers == 30)
print("Where (30):", where_result)  # Output: (array([2]),)


numbers = np.array([2, 4, 6, 8, 10])
result = np.where(numbers > 0)
print(result)  # Output: (array([0, 1, 2, 3, 4]),)


conditional_array = np.array([1, 2, 3, 4, 5])
# Using np.where to find indices of elements greater than 3
indices = np.where(conditional_array > 3)
print("Indices of elements greater than 3:", indices)  # Output: (array([3, 4]),)


#adding data
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# Adding two arrays
result = arr1 + arr2
print("Result of adding two arrays:", result)  # Output: [5 7 9]

combined_array = np.concatenate((arr1, arr2))
print("Combined array:", combined_array)  # Output: [1 2 3 4 5 6]


arr1=np.array([[1, 2], [3, 4]])
arr2=np.array([[5, 6], [7, 8]])
result = arr1 + arr2
print("Result of adding two 2D arrays:\n", result)  # Output: [[ 6  8] [10 12]]
arr1.shape == arr2.shape
print("Are the shapes of arr1 and arr2 equal?", arr1.shape == arr2.shape)  # Output: True

#row
#in vertical
original = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_row = np.array([[10, 11, 12]])
# Adding a new row to the original array
added_row_array = np.vstack((original, new_row))
print("Array after adding a new row:\n", added_row_array)


#in horizontal
original = np.array([[1, 2], [3, 4]])
new_column = np.array([[5], [6]])
# Adding a new column to the original array
added_column_array = np.hstack((original, new_column))
print("Array after adding a new column:\n", added_column_array)


