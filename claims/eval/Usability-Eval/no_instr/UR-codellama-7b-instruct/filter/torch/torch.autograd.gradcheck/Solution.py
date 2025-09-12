
import torch
import numpy as np

def check_gradients(inputs):
    # Compute finite differences approximations of gradients
    eps = 1e-5
    inputs_fd = inputs.detach().clone()
    for i in range(len(inputs)):
        inputs_fd[i] += eps
        grad1 = (loss_fn(model(inputs_fd)) - loss_fn(model(inputs))) / eps
        inputs_fd[i] -= 2 * eps
        grad2 = (loss_fn(model(inputs_fd)) - loss_fn(model(inputs))) / (-2 * eps)
        analytical_grad = (grad1 - grad2) / (2 * eps)
    
    # Compute analytical gradients of model with requires_grad=True. inputs
    inputs_ag = inputs.clone().detach()
    inputs_ag.requires_grad_(True)
    analytical_grad = torch.autograd.grad(loss_fn(model(inputs)), inputs, grad_outputs=torch.ones_like(loss_fn(model(inputs))))[0]
    
    # Compute error in finite differences vs analytical gradients
    diff = (analytical_grad - analytical_grad_fd) / analytical_grad
    err = np.max(np.abs(diff))
    print("Maximum error:", err)
    
    if err > 1e-3:
        print("Error is too large!")
