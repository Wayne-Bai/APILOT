import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6], dtype=np.float32)
c = np.array([[1, 2], [3, 4]], order='F')

pointer_a = a.__array_interface__['data'][0]
pointer_b = b.__array_interface__['data'][0]
pointer_c = c.__array_interface__['data'][0]

print(pointer_a)
print(pointer_b)
print(pointer_c)