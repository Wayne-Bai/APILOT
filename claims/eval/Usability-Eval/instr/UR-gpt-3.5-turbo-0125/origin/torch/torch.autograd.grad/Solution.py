
import torch

def compute_input_gradients(outputs, inputs):
    gradients = torch.autograd.grad(outputs, inputs, torch.ones_like(outputs))[0]
    return gradients
