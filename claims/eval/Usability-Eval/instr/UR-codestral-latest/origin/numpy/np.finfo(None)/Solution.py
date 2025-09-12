import numpy as np

# The smallest positive value that can be represented by numpy float16
print("Min value for float16:", np.finfo(np.float16).tiny)

# The smallest positive value that can be represented by numpy float32
print("Min value for float32:", np.finfo(np.float32).tiny)

# The smallest positive value that can be represented by numpy float64
print("Min value for float64:", np.finfo(np.float64).tiny)

# The largest value that can be represented by numpy float16
print("Max value for float16:", np.finfo(np.float16).max)

# The largest value that can be represented by numpy float32
print("Max value for float32:", np.finfo(np.float32).max)

# The largest value that can be represented by numpy float64
print("Max value for float64:", np.finfo(np.float64).max)
