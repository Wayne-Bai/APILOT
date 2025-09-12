import torch

# Create a sample tensor
tensor = torch.tensor([
    [5, 6, 7],
    [8, 9, 10],
    [11, 12, 13]
])

# Create a mask that is broadcastable with the shape of the tensor
mask = torch.tensor([
    [True, False, True],
    [False, True, False],
    [True, True, False]
])

# Define the filling value
fill_value = 99

# Fill elements of the tensor with the fill_value where the mask is True
tensor.masked_fill_(mask, fill_value)

print(tensor)
