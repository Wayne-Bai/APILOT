import torch

def detach_tensor(tensor):
    """
    Detaches the Tensor from the graph that created it, making it a leaf.
    Views cannot be detached in-place.

    Args:
        tensor (torch.Tensor): The tensor to detach.

    Returns:
        torch.Tensor: The detached tensor.
    """
    return tensor.detach()

# Example usage:
tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
detached_tensor = detach_tensor(tensor)
print(detached_tensor)
