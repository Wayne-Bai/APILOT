import numpy as np

# Sample array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate cumulative product along axis=0 (columns)
cumulative_product_columns = np.cumprod(arr, axis=0)

# Calculate cumulative product along axis=1 (rows)
cumulative_product_rows = np.cumprod(arr, axis=1)

print("Cumulative product along columns:")
print(cumulative_product_columns)

print("\nCumulative product along rows:")
print(cumulative_product_rows)
