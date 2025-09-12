import torch

# Define a tensor
x = torch.tensor([1.0, 2.0, 3.0])

# Define a function to compute the sum of gradients
def compute_sum_of_gradients(y):
    # Compute the gradient of y with respect to x
    dy_dx = torch.tensor([0.0, 0.0, 0.0])
    # Compute the sum of gradients
    sum_of_gradients = torch.sum(dy_dx)
    return sum_of_gradients

# Compute the sum of gradients
sum_of_gradients = compute_sum_of_gradients(x)

print(sum_of_gradients)
