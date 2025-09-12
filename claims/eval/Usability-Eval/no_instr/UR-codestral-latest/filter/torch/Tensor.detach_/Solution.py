import torch # Importing the torch library

# Creating a tensor that requires gradient
tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Detaching the tensor from the computation graph
tensor_detached = tensor.detach()
