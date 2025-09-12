import torch

# Define the input tensors
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0])
other_tensor = torch.tensor([2.0, 3.0, 4.0, 5.0])

# Divide each element of the input tensor by the corresponding element of the other tensor
output_tensor = input_tensor / other_tensor

print(output_tensor)
