import torch

# Assuming input1 and input2 are torch tensors
input1 = torch.tensor([1.0, 2.0, 3.0])
input2 = torch.tensor([4.0, 5.0, 6.0])

# Dividing each element of input1 by the corresponding element of input2
result = input1 / input2

print(result)
