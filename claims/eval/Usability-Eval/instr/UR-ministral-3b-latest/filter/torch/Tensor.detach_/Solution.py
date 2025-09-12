import torch

# Sample tensor
x = torch.tensor([1.0, 2.0, 3.0])
print("Original Tensor:", x)

# Detach the tensor
x_det = x.detach()
print("Detached Tensor:", x_det)

# Check if detached tensor is in the computation graph
print("\nIs the Detached Tensor in the Computation Graph?", x_det in x.requires_grad)

# Perform operations on the detached tensor without mutating original tensor graph
with torch.no_grad():
    y = x_det + 1
print("New Tensor computed on the Detached Tensor:", y)
