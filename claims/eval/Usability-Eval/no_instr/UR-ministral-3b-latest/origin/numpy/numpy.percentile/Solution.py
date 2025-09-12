import numpy as np

# Example usage
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axis = 1  # Noting that axis is 1, so we are looking at the rows in this example.
q = 50  # We are looking for the 50th percentile

percentile = np.percentile(data, q, axis=axis)
print(percentile)
