
import torch
import numpy as np

# Create a random tensor
tensor = torch.randn(3, 3)

# Convert the tensor to a NumPy ndarray
numpy_ndarray = tensor.numpy()

print(type(numpy_ndarray))  # Verifies the type of the converted array is numpy.ndarray
