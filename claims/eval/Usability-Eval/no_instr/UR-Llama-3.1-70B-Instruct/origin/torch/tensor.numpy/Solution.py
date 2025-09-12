import torch

def tensor_to_numpy(tensor):
    return tensor.detach().numpy()

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Convert tensor to numpy array
numpy_array = tensor_to_numpy(tensor)

print("Original Tensor:")
print(tensor)
print("Converted NumPy Array:")
print(numpy_array)
