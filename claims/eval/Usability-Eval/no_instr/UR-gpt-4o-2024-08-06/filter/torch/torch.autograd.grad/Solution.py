import torch

def compute_gradients(inputs, outputs):
    '''
    Computes and returns the sum of gradients of outputs with respect to the inputs.

    Args:
        inputs (torch.Tensor): The input tensor with `requires_grad=True`.
        outputs (torch.Tensor): The output tensor which is a function of `inputs`.

    Returns:
        torch.Tensor: Sum of gradients of `outputs` with respect to `inputs`.
    '''
    # Ensure the inputs require gradient
    if not inputs.requires_grad:
        inputs.requires_grad = True
    
    # Computes the gradients
    gradients = torch.autograd.grad(outputs, inputs, grad_outputs=torch.ones_like(outputs), create_graph=True)[0]
    
    # Sum of gradients
    gradients_sum = gradients.sum()

    return gradients_sum

# Example usage
inputs = torch.tensor([2.0, 3.0], requires_grad=True)
outputs = inputs**2
grad_sum = compute_gradients(inputs, outputs)
print(grad_sum)  # to illustrate usage, this should print the sum of gradients
