
import numpy as np

arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
pointer = arr.data.tobytes()  # A pointer to the memory area of the array as a Python integer
print(pointer)
