import torch

def compute_gradients_sum(model, inputs, outputs):
    """
    This function computes and returns the sum of gradients of outputs with respect to the inputs.
    
    Args:
        model (torch.nn.Module): The PyTorch model to compute gradients for.
        inputs (torch.Tensor): The input tensor to the model.
        outputs (torch.Tensor): The output tensor from the model.
    
    Returns:
        torch.Tensor: The sum of gradients of outputs with respect to the inputs.
    """
    
    # Compute the loss (in this case, mean squared error) between the outputs and a constant tensor
    loss = (outputs - torch.zeros_like(outputs)).pow(2).mean()
    
    # Zero the gradients of the model
    model.zero_grad()
    
    # Backward pass: compute gradients
    loss.backward()
    
    # Get the gradients of the model with respect to the inputs
    gradients = inputs.grad
    
    # Sum the gradients along the desired axis (in this case, all axes)
    gradients_sum = gradients.sum(dim=(0, 2, 3))
    
    return gradients_sum

# Example usage:
model = torch.nn.Linear(5, 5)
input_tensor = torch.randn(1, 5, 5, 5, requires_grad=True)
output_tensor = model(input_tensor)

gradients_sum = compute_gradients_sum(model, input_tensor, output_tensor)
print(gradients_sum)
