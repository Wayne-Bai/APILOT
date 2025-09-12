import torch

def tensor_to_numpy(tensor):
    # Ensure the tensor is on the CPU if it is a CUDA tensor
    if tensor.is_cuda:
        tensor = tensor.cpu()
    
    # Use the .numpy() method to convert the tensor to a NumPy ndarray
    return tensor.numpy()

# Example usage:
tensor = torch.tensor([1.0, 2.0, 3.0])
numpy_array = tensor_to_numpy(tensor)
print(numpy_array)
