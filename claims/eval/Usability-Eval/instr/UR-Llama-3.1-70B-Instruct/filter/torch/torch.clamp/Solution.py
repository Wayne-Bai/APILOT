import torch

def torch_clamp(input_tensor, min_val, max_val):
    """
    Clamps all elements in input into the range [min_val, max_val].
    
    Args:
        input_tensor (torch.Tensor): Input tensor to be clamped.
        min_val (float): Minimum value of the range.
        max_val (float): Maximum value of the range.
    
    Returns:
        torch.Tensor: Clamped tensor.
    """
    return torch.where(input_tensor < min_val, min_val * torch.ones_like(input_tensor), 
                       torch.where(input_tensor > max_val, max_val * torch.ones_like(input_tensor), input_tensor))

# Example usage
if __name__ == "__main__":
    input_tensor = torch.tensor([-1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=torch.float32)
    min_val = 2.5
    max_val = 5.5
    
    clamped_tensor = torch_clamp(input_tensor, min_val, max_val)
    
    print("Original Tensor:")
    print(input_tensor)
    
    print("\nClamped Tensor:")
    print(clamped_tensor)
