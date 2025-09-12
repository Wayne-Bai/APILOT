import torch

def tensor_to_numpy(tensor):
    # Ensure the tensor is on CPU, detach and convert to numpy
    return tensor.cpu().detach().numpy()

# Example usage:
# Create a torch tensor
t = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
# Convert it to a numpy ndarray
np_array = tensor_to_numpy(t)
print(np_array)
