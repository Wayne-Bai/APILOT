import torch

# Assume that 'tensors' is a list of torch tensors and 'leaves' is a list of nodes in the computation graph
# The 'compute_gradients' function computes the gradients of the given tensors with respect to the leaves
def compute_gradients(tensors, leaves):
    gradients = [torch.zeros_like(tensor) for tensor in tensors]
    for leaf in leaves:
        for tensor in tensors:
            if leaf in tensor.grad:
                gradients[tensors.index(tensor)] += tensor.grad[leaf]
    return gradients
