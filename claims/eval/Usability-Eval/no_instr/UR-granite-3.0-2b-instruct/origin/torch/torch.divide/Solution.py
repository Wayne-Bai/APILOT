import torch

# Assume we have two tensors
tensor1 = torch.tensor([2.0, 4.0, 6.0])
tensor2 = torch.tensor([1.0, 2.0, 3.0])

# Divide each element of tensor1 by the corresponding element of tensor2
result = tensor1 / tensor2

print(result)
