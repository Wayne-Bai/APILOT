# Import the necessary library
import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3], requires_grad=True)

# Print the initial grad fn
print("Before detaching: ", tensor.grad_fn)

# Detach the tensor
detached_tensor = tensor.detach()

# Print the grad fn after detaching
print("After detaching: ", detached_tensor.grad_fn)

# As you can see, the detached tensor does not have a grad_fn, 
# meaning it is no longer part of the computation graph.
