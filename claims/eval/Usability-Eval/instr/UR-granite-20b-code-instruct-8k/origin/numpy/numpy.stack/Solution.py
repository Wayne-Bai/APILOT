import numpy as np

# User defined variables
arrays = ...  # Replace with the sequence of arrays to be joined
axis = ...  # Replace with the axis along which the arrays will be joined

# Join the arrays along the specified axis
result = np.stack(arrays, axis=axis)

# Display the result
print(result)
