import torch

def divide_tensors(input_tensor, other_tensor):
    if input_tensor.shape != other_tensor.shape:
        raise ValueError("The shapes of the input tensors must match.")
    return input_tensor / other_tensor

# Example usage
input_tensor = torch.tensor([[4.0, 2.0], [6.0, 3.0]])
other_tensor = torch.tensor([[2.0, 1.0], [3.0, 1.5]])
result_tensor = divide_tensors(input_tensor, other_tensor)

print(result_tensor)
