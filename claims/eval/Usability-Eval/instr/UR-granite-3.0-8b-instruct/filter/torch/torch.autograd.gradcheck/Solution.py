import torch

def check_gradients(model, inputs, outputs, epsilon=1e-5):
    for name, param in model.named_parameters():
        if param.requires_grad and param.is_floating_point_or_complex():
            analytical_grad = torch.autograd.grad(outputs, param, retain_graph=True)[0]
            numerical_grad = torch.autograd.grad(outputs, param, retain_graph=True, create_graph=True)[0]
            numerical_grad = (numerical_grad.detach() - outputs.detach()) / epsilon
            assert torch.allclose(analytical_grad, numerical_grad, atol=1e-3), f"Gradient check failed for {name}"
