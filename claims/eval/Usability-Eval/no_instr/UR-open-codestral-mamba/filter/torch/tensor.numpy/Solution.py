import torch
import numpy as np

# Let's create a tensor using PyTorch
tensor = torch.tensor([[1, 2], [3, 4]])

# Then use .numpy() method to convert the tensor to NumPy ndarray
numpy_array = tensor.numpy()

print(numpy_array)
