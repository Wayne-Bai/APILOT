import numpy as np

# Just an example array
a = np.array(((1, 2), (3, 4)))

# Use np.pad to pad the array with a padding of 2 in both dimensions
# 'constant' specifies the padding mode, and 0 specifies the constant value used for padding
padded_a = np.pad(a, ((2, 2), (2, 2)), 'constant', constant_values=0)

print(padded_a)
