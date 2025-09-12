import torch

def check_gradients(model, inputs, epsilon=1e-6):
    # Ensure the model is in evaluation mode to not affect batchnorm or other training-specific layers
    model.eval()
    
    # Loop through all parameters in the model and inputs
    for i, x in enumerate(inputs):
        if x.dtype.is_floating_point or x.dtype.is_complex:
            if x.requires_grad:
                # Save the original value of x to restore later
                x_original = x.clone().detach()
                
                # Creating a matrix to store gradients
                analytical_grad = torch.zeros_like(x)
                finite_diff_grad = torch.zeros_like(x)
                
                # Iterate over all elements of x
                for idx in torch.ndindex(x.shape):
                    # Perturb x slightly positively
                    x[idx] += epsilon
                    outputs_pos = model(*inputs)
                    loss_pos = outputs_pos.sum()
                    loss_pos.backward()
                    
                    # Store the computed gradients
                    grad_pos = x.grad.clone().detach()
                    
                    # Restore x and clear gradient
                    x.grad = None
                    x[idx] = x_original[idx]
                    
                    # Perturb x slightly negatively
                    x[idx] -= epsilon
                    outputs_neg = model(*inputs)
                    loss_neg = outputs_neg.sum()
                    loss_neg.backward()
                    
                    # Compute gradients from finite differences
                    grad_neg = x.grad.clone().detach()
                    finite_diff = (grad_pos - grad_neg) / (2 * epsilon)
                    
                    # Store in our finite difference gradient matrix
                    finite_diff_grad[idx] = finite_diff
                    
                    # Restore x completely
                    x.grad = None
                    x[idx] = x_original[idx]
                
                # Getting analytical gradient by forwarding and backward with untouched input
                outputs = model(*inputs)
                loss = outputs.sum()
                loss.backward()
                analytical_grad = x.grad
                
                # Print out the comparison results
                print(f'Analytical Gradient for input {i}: \n{analytical_grad}')
                print(f'Finite Difference Gradient for input {i}: \n{finite_diff_grad}')
                print(f'Difference for input {i}: \n{analytical_grad - finite_diff_grad}\n')

# Testing the function (Assuming a model and inputs are defined elsewhere with appropriate requires_grad settings)
# Example usage:
# model = SomeModel()
# inputs = [torch.randn(2, 2, requires_grad=True)]
# check_gradients(model, inputs)
