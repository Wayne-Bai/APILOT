import torch

def tensor_to_ndarray(tensor):
    return tensor.numpy()

# Example usage:
tensor = torch.tensor([1.0, 2.0, 3.0])
ndarray = tensor_to_ndarray(tensor)
print(ndarray)
