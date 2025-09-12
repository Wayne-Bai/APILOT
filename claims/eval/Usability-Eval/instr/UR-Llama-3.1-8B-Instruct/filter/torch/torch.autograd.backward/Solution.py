import torch

# Define some sample tensors
x1 = torch.randn(2, 3)
x2 = torch.randn(2, 3)

# Place the tensors in a autograd context manager
with torch.autograd.enable_grad() as g1:
    # Compute the sum of x1 and x2
    y = x1 + x2
    
# Since x1 and x2 are the inputs to the computation, torch.autograd.grad
# can't find their gradients. We also need the loss w.r.t the y leaves
y.sum().backward()
#detach() find all root computations up to the Leafs
x1_sum, x2_sum = x1.detach(), x2.detach() 
x1_grads = torch.autograd.grad(y.sum(), x1_sum)[0]
x2_grads = torch.autograd.grad(y.sum(), x2_detach().sum())[0] 
print(x1_sum + x2_sum)
# Compute the sum of gradients of x1 and x2 with respect to the graph leaves
print(x1_grads + x2_grads)
