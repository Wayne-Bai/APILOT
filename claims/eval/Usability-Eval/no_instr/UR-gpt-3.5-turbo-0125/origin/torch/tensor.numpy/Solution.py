
import torch
import numpy as np

# Create a tensor using torch
tensor = torch.randn(2, 3)

# Convert the torch tensor to a NumPy ndarray
numpy_array = tensor.numpy()
print(numpy_array)
