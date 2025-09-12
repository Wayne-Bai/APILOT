import torch
import torch.nn as nn

def compute_gradients_sum(model, X, y):
    """
    This function computes and returns the sum of gradients of outputs with respect to the inputs.
    
    Parameters:
    model (nn.Module): A PyTorch neural network model.
    X (Tensor): Input tensor.
    y (Tensor): Ground truth tensor.
    
    Returns:
    Tensor: The sum of gradients of outputs with respect to the inputs.
    """
    
    # Set the model to training mode
    model.train()
    
    # Create a gradient accumulator
    params = nn.Parameters(model)
    gradients = torch.zeros_like(params)
    
    # Forward pass
    output = model(X)
    
    # Compute the loss
    criterion = nn.CrossEntropyLoss()
    loss = criterion(output, y)
    
    # Backward pass
    loss.backward()
    
    # Compute the gradients of output with respect to the parameters
    gradient = model.parameters()
    
    # Accumulate gradients
    for p in gradients:
        p.data.add_(p.grad.data)
    
    # Return the sum of gradients
    return gradients

# Example usage
if __name__ == "__main__":
    # Initialize the model
    model = nn.Sequential(
        nn.Linear(784, 128),
        nn.ReLU(),
        nn.Linear(128, 10)
    )
    
    # Initialize the inputs and ground truth
    X = torch.randn(100, 784)
    y = torch.randint(0, 10, (100,))
    
    # Compute the sum of gradients
    gradients = compute_gradients_sum(model, X, y)
    
    # Print the gradients
    for i, param in enumerate(model.parameters()):
        print(f"Gradient {i+1}: {param.grad}")
