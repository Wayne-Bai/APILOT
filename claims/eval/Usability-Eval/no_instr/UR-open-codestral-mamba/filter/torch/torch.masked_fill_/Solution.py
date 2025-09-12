import torch

# create a tensor of shape (5, 5)
tensor = torch.rand(5, 5)
print("Original Tensor:\n", tensor)

# create a boolean mask of shape (5, 5)
mask = tensor > 0.5 # this is just an example condition, replace with your own condition
print("\nMask:\n", mask.int())

# define a value that we shall use to fill the tensor
value = 1.0 # replace with your own value

# fill the tensor with the defined value where the mask is True
tensor.masked_fill_(mask, value)
print("\nTensor After Filling Masked Values:\n", tensor)
