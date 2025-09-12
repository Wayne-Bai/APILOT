import torch

# Define a tensor
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Define a mask
mask = torch.tensor([[True, False, True], [False, True, False]])

# Define the value to fill
value = 10

# Fill the tensor with value where mask is True
result = torch.where(mask, torch.full_like(tensor, value), tensor)

print("Original Tensor:")
print(tensor)
print("Mask:")
print(mask)
print("Result:")
print(result)
