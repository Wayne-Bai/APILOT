import torch

# Define the tensor that you want to convert to a NumPy array
tensor = torch.randn(5, 3)

# Use the 'to_numpy' method to convert the tensor to a NumPy array
array = tensor.to_numpy()

print(array)