
import torch

def compute_input_gradients(inputs, outputs):
    gradients = torch.autograd.grad(outputs, inputs, grad_outputs=torch.ones_like(outputs), create_graph=True)
    total_gradients = sum([gradient.sum() for gradient in gradients])
    
    return total_gradients
