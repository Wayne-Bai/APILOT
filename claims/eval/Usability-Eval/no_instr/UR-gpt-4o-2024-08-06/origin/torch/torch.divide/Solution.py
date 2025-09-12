import torch

# Define two example tensors
input_tensor = torch.tensor([4.0, 9.0, 16.0, 25.0])
other_tensor = torch.tensor([2.0, 3.0, 4.0, 5.0])

# Perform element-wise division
result_tensor = input_tensor / other_tensor

# Print the result
print(result_tensor)
