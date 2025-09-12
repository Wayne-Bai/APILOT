
import torch

input = torch.tensor([10.0, 20.0, 30.0])
other = torch.tensor([2.0, 4.0, 6.0])

result = torch.div(input, other)

print(result)
