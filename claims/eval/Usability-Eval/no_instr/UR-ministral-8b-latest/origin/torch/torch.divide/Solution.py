import torch

# Function to divide each element of input tensor by the corresponding element of another tensor
def divide_elements(input_tensor, other_tensor):
    # Ensure both tensors have the same shape
    assert input_tensor.shape == other_tensor.shape, "Input tensors must have the same shape"
    # Perform element-wise division
    result_tensor = input_tensor / other_tensor
    return result_tensor

# Example usage
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
other_tensor = torch.tensor([[2.0, 1.0], [1.5, 2.0]], dtype=torch.float32)
result = divide_elements(input_tensor, other_tensor)
print(result)
