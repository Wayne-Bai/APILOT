import torch

def compute_gradient_sum(input_tensor, model):
    # Ensure the input tensor requires gradients
    input_tensor.requires_grad_(True)
    
    # Forward pass
    output = model(input_tensor)
    
    # Zero the gradients before the backward pass
    model.zero_grad()
    
    # Compute gradients with respect to inputs
    output.sum().backward()
    
    # Sum of gradients of outputs with respect to inputs
    gradient_sum = input_tensor.grad.sum()
    
    return gradient_sum

# Example usage:
# Define a simple model for demonstration
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

# Create an instance of the model and an input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 10)

# Compute the sum of gradients
result = compute_gradient_sum(input_tensor, model)
print(result)
