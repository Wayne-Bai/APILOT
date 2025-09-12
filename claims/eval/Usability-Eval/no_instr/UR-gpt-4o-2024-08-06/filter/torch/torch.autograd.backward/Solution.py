import torch

# Define a simple computational graph with some operations
x = torch.tensor(3.0, requires_grad=True)
y = torch.tensor(4.0, requires_grad=True)

# Perform some operations
z = x * y + y ** 2

# Compute gradients
z.backward()

# Function to compute the sum of gradients with respect to graph leaves
def sum_of_gradients(*tensors):
    sum_grad = 0
    for t in tensors:
        if t.grad is not None:
            sum_grad += t.grad.sum()
    return sum_grad

# Usage example: Compute the sum of gradients
gradient_sum = sum_of_gradients(x, y)
print("Sum of gradients:", gradient_sum)
