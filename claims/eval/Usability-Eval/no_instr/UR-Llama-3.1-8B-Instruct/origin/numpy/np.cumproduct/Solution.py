import numpy as np

# Define a 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the cumulative product along axis 0 (rows)
cumulative_product_rows = np.cumprod(array, axis=0)

# Calculate the cumulative product along axis 1 (columns)
cumulative_product_cols = np.cumprod(array, axis=1)

print("Cumulative product along axis 0 (rows):")
print(cumulative_product_rows)

print("\nCumulative product along axis 1 (columns):")
print(cumulative_product_cols)
