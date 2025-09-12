
import torch

# Create a sample tensor
tensor = torch.randn(3, 4)
print(tensor)
# >>>> torch.Size([3, 4])
# >>>> tensor([[0.8595, -1.4266,  1.0767, -1.1642],
# >>>> [ 0.9654, -0.2324, -1.1642,  0.3578],
# >>>> [-1.3430, -1.3271, -0.2324,  0.7783]])

# Create a boolean mask
mask = torch.BoolTensor([[True, False, True, False],
                         [False, True, False, True],
                         [True, False, True, False]])
print(mask)
# >>>> tensor([[ True, False,  True, False],
# >>>> [False,  True, False,  True],
# >>>> [ True, False,  True, False]])

# Index the input tensor according to the boolean mask
new_tensor = tensor[mask]
print(new_tensor)
# >>>> tensor([0.8595, -1.4266,  1.0767])
