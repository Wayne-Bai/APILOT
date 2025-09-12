import numpy as np

# creating a random array for the demonstration
array = np.random.rand(3, 4)

# getting the indices of minimum values along an axis
# here, axis = 0, which means along the columns
min_indices = np.argmin(array, axis=0)

print("Indices of minimum values along the columns: ", min_indices)

# If you want to find the indices along the rows, you can set axis = 1
min_indices_rows = np.argmin(array, axis=1)

print("Indices of minimum values along the rows: ", min_indices_rows)
