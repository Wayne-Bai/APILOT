import numpy as np

# Create a sample array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Using np.prod() function to calculate the product of array elements over a given axis
# For product along rows (axis = 1)
product_arr_rows = np.prod(arr, axis = 1)

# For product along columns (axis = 0)
product_arr_cols = np.prod(arr, axis = 0)

# Alternatively, you can use axis parameter to specify the axis
# For product along rows (axis = 1)
product_arr_rows_alternate = np.prod(arr, axis=1)

# For product along columns (axis = 0)
product_arr_cols_alternate = np.prod(arr, axis=0)

# Print the results
print("Product along rows:")
print(product_arr_rows)
print("\nProduct along columns:")
print(product_arr_cols)
