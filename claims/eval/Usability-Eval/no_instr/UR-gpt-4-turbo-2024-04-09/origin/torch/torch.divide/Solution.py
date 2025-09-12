import torch

# Define the tensors
input_tensor = torch.tensor([10.0, 20.0, 30.0])
other_tensor = torch.tensor([2.0, 5.0, 10.0])

# Divide each element
result_tensor = torch.div(input_tensor, other_tensor)

print(result_tensor)
