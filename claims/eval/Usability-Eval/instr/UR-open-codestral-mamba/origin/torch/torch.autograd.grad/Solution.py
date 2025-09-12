import torch

def sum_gradients(outputs):
    """
    Function to compute and return the sum of gradients of outputs with respect to the inputs
    """
    if not isinstance(outputs, tuple):
        outputs = (outputs, )
    grads = torch.autograd.grad(outputs, (outputs[0].grad_fn.inputs[0], ))
    return sum(g.grad_fn.inputs[0].grad for g in grads)
