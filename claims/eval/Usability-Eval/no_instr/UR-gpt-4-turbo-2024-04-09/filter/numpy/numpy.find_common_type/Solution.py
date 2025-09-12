import numpy as np

# Example data types
dtype1 = np.int32
dtype2 = np.float64

# Determine common type following standard coercion rules
common_type = np.find_common_type([dtype1, dtype2], [])
print("The common data type is:", common_type)
