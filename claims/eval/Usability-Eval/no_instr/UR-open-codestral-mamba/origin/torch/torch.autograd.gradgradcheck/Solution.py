import torch

def check_gradients_analytical_finite_difference(loss_fn, model):
    # Zero all gradients
    model.zero_grad()

    # Get current model parameters
    params = filter(lambda p: p.requires_grad, model.parameters())

    # Calculate loss and gradient w.r.t parameters using torch.autograd
    loss = loss_fn(model)
    grad_autograd = torch.autograd.grad(loss, params)

    # Calculate finite differences for each parameter
    eps = 1e-6
    grad_finite_diff = []
    for param in params:
        # Save current parameter value
        original_value = param.data.detach().clone()

        # Calculate lower value for finite difference
        param.required_grad_ = True
        lower_value = original_value - eps
        param.data = lower_value
        loss_lower = loss_fn(model)

        # Calculate upper value for finite difference
        upper_value = original_value + eps
        param.data = upper_value
        loss_upper = loss_fn(model)

        # Calculate finite difference and append to list
        finite_diff = (loss_upper - loss_lower) / (2 * eps)
        grad_finite_diff.append(finite_diff)

        # Restore original parameter value
        param.data = original_value
        param.required_grad_ = True

    # Compare the gradients calculated with autograd and with finite differences
    for grad_a, grad_fd in zip(grad_autograd, grad_finite_diff):
        assert torch.allclose(grad_a, grad_fd, atol=1e-5), 'Gradients do not match'
    return True
