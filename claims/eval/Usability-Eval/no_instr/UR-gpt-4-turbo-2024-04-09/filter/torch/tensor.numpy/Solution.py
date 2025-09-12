import torch

def tensor_to_numpy(tensor):
    return tensor.numpy()

# Example usage:
tensor = torch.rand(3, 3)
numpy_array = tensor_to_numpy(tensor)
print(numpy_array)
