
import torch

# Initialize the input and other tensors
input = torch.tensor([1, 2, 3])
other = torch.tensor([4, 5, 6])

# Divide each element of the input by the corresponding element of other
result = torch.div(input, other)

# Print the result
print(result)
