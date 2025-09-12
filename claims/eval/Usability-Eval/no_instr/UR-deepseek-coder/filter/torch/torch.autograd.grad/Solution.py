import torch

def sum_of_gradients(outputs, inputs):
    # Ensure the inputs require gradients
    inputs = [input.requires_grad_() for input in inputs]
    
    # Compute the gradients of outputs with respect to inputs
    gradients = torch.autograd.grad(outputs, inputs, create_graph=True)
    
    # Sum the gradients
    sum_grads = sum(grad.sum() for grad in gradients)
    
    return sum_grads

# Example usage:
# inputs = [torch.tensor([1.0, 2.0], requires_grad=True), torch.tensor([3.0, 4.0], requires_grad=True)]
# outputs = inputs[0] * inputs[1]
# result = sum_of_gradients(outputs, inputs)
# print(result)
