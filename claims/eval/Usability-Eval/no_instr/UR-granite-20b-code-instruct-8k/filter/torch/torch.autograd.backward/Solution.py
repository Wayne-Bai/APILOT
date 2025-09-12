
import torch

# Define your tensors and gradients here
tensor1 = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
tensor2 = torch.tensor([4.0, 5.0, 6.0], requires_grad=True)

# Compute the sum of gradients
sum_grad = torch.sum(tensor1) + torch.sum(tensor2)

# Backpropagate the gradients
sum_grad.backward()

# Print the gradients
print(tensor1.grad)
print(tensor2.grad)
