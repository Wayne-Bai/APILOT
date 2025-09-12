import torch

# Assume we have some tensors for which we want to compute the gradients
tensors = [torch.tensor([i.float()], requires_grad=True) for i in range(5)]

# Assume we have a function that uses these tensors
def compute_loss(tensors):
    return sum([t**2 for t in tensors])

# Compute the loss
loss = compute_loss(tensors)

# Compute the gradients
loss.backward()

# Sum the gradients of all tensors
gradients_sum = sum([t.grad.sum() for t in tensors])

print(gradients_sum)
