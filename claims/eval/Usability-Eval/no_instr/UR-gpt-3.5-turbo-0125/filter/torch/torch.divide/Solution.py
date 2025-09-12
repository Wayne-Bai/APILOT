import torch

input = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([0.5, 1.0, 2.0])

result = torch.div(input, other)
print(result)
