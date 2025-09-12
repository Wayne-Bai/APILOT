import torch

def index_with_boolean_mask(input_tensor, mask):
    # Ensure the mask is a boolean tensor
    if not mask.dtype == torch.bool:
        raise ValueError("The mask must be a boolean tensor.")

    # Index the input tensor using the boolean mask
    indexed_tensor = input_tensor[mask]
    
    return indexed_tensor

# Example usage
input_tensor = torch.tensor([10, 20, 30, 40, 50])
mask = torch.tensor([True, False, True, False, True])  # Boolean mask

result = index_with_boolean_mask(input_tensor, mask)
print(result)  # Output will be: tensor([10, 30, 50])
