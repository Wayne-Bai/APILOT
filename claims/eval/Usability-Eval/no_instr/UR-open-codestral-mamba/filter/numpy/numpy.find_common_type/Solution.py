import numpy as np

# Input arrays
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array(['1', '2', '3'], dtype=np.unicode_)
arr3 = np.array([1.2, 2.3, 3.1], dtype=np.float64)

# Coerce the arrays to a common type
common_type = np. promotions.promote_types(arr1.dtype.type, (arr2.dtype.type, arr3.dtype.type))

# Convert arrays to the common type
arr1 = arr1.astype(common_type)
arr2 = arr2.astype(common_type)
arr3 = arr3.astype(common_type)

print("Common Type: ", common_type)
print("Coerced Array-1: ", arr1)
print("Coerced Array-2: ", arr2)
print("Coerced Array-3: ", arr3)
