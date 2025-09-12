import torch

# Example input tensors
input_tensor = torch.tensor([10.0, 20.0, 30.0])
other_tensor = torch.tensor([2.0, 4.0, 5.0])

# Element-wise division
result_tensor = torch.div(input_tensor, other_tensor)

# Print the result
print(result_tensor)
