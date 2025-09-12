import torch

def detach_tensor(tensor):
    # Detach the tensor from the computation graph
    detached_tensor = tensor.detach()
    
    # Ensure the detached tensor is a leaf
    detached_tensor.requires_grad_(False)
    
    return detached_tensor

# Example usage
tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
detached_tensor = detach_tensor(tensor)

print("Original Tensor:", tensor)
print("Detached Tensor:", detached_tensor)
