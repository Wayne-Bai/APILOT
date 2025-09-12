import torch

# Define a tensor
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Define a function to compute the sum of gradients
def compute_gradients(x):
    # Compute the sum of gradients
    sum_of_gradients = torch.sum(x)
    return sum_of_gradients

# Compute the sum of gradients
sum_of_gradients = compute_gradients(x)

# Print the sum of gradients
print(sum_of_gradients)
