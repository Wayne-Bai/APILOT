import torch
tensor = torch.randn(2, 3, requires_grad=True)
print(tensor)
tensor_detached = tensor.detach()
print(tensor_detached)
