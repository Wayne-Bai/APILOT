import torch

def compute_sum_of_gradients(model, inputs):
    # Ensure the inputs require gradients
    inputs.requires_grad_(True)
    
    # Perform a forward pass
    outputs = model(inputs)
    
    # Compute gradients with respect to inputs
    outputs.sum().backward()  # Sum of outputs to compute the overall gradient
    
    # Retrieve gradients of the outputs with respect to inputs
    gradients = inputs.grad
    
    return gradients.sum() if gradients is not None else None

# Example usage
# Define a simple model
class SimpleModel(torch.nn.Module):
    def forward(self, x):
        return x ** 2  # A simple operation

# Create model and sample input
model = SimpleModel()
inputs = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Compute sum of gradients
gradient_sum = compute_sum_of_gradients(model, inputs)
print(gradient_sum)
