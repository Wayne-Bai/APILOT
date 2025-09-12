import torch

# Create an example mask tensor with boolean values
mask = torch.tensor([
    [True, False, False],
    [False, True, True]
])

# The source tensor from which we will copy the elements
source = torch.tensor([
    [10, 20, 30],
    [40, 50, 60]
])

# The target tensor where elements will be copied to
target = torch.tensor([
    [1, 1, 1],
    [1, 1, 1]
])

# Use masked_select and masked_fill to copy elements from source to target
# Step 1: Select elements from source using the mask
selected_elements = source[mask]

# Step 2: Create a copy of target and fill it with selected elements at masked positions
target_masked_indices = mask.nonzero(as_tuple=True)
target[target_masked_indices] = selected_elements

print("Modified target tensor:")
print(target)
