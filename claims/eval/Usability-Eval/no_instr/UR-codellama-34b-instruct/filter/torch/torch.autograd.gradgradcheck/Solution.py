
import torch
from torch.autograd import gradcheck

def check_gradients(model, inputs, grad_outputs):
    # Compute analytical gradients using autograd
    analytical_grads = torch.autograd.functional.backward(inputs, grad_outputs)

    # Compute numerical gradients using finite differences
    numerical_grads = compute_numerical_gradients(model, inputs, grad_outputs)

    # Check that the analytical and numerical gradients match
    for name, ana_grad in analytical_grads.items():
        num_grad = numerical_grads[name]
        assert torch.allclose(ana_grad, num_grad), "Gradient mismatch for {}".format(name)
