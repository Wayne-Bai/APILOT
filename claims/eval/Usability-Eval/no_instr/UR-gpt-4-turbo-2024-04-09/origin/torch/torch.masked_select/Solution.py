import torch

def index_tensor_with_mask(input_tensor, mask):
    # Ensure the mask is of boolean type
    if mask.dtype != torch.bool:
        raise ValueError("Mask must be a boolean tensor.")
    
    # Indexing the tensor with mask
    indexed_tensor = input_tensor[mask]
    return indexed_tensor

# Example usage
input_tensor = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True], dtype=torch.bool)
result = index_tensor_with_mask(input_tensor, mask)
print(result)  # Output will be tensor([1, 3, 5])
