
import numpy as np
try:
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr.shape)  # Output: (2, 3)
    print(arr.ndim)  # Output: 2
    print(arr.size)  # Output: 6
    print(arr.dtype)  # Output: int64
except np.AxisError as e:
    print(f"AxisError: {e}")
