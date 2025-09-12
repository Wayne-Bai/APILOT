import torch

# Example tensor and mask
tensor = torch.zeros(3, 4)
mask = torch.tensor([[True, False, True, False],
                     [False, True, False, True],
                     [True, True, False, False]])

# Value to fill where mask is True
value = 5

# Fill the tensor where the mask is True
tensor[mask] = value

print(tensor)
