import numpy as np

class MyArray:
    def __init__(self, data, shape):
        self.data = data
        self.shape = shape

    def __getattr__(self, name):
        if name == 'ndim':
            return len(self.shape)
        return getattr(self.data, name)

# Example usage:
data = np.array([1, 2, 3, 4, 5])
shape = (5,)
arr = MyArray(data, shape)
print(arr.ndim)  # Output: 1
