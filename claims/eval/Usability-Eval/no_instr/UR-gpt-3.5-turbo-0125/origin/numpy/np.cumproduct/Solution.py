
import numpy as np

# Create a sample 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Calculate cumulative product along axis 0
cum_prod_axis0 = np.cumprod(arr, axis=0)

print("Cumulative product along axis 0:")
print(cum_prod_axis0)

# Calculate cumulative product along axis 1
cum_prod_axis1 = np.cumprod(arr, axis=1)

print("\nCumulative product along axis 1:")
print(cum_prod_axis1)
