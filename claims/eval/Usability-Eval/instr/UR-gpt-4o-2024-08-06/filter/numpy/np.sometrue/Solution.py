import numpy as np

# Example array
array = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

# Test if any element in each column evaluates to True
any_in_columns = np.any(array, axis=0)
print("Any True in columns:", any_in_columns)

# Test if any element in each row evaluates to True
any_in_rows = np.any(array, axis=1)
print("Any True in rows:", any_in_rows)
