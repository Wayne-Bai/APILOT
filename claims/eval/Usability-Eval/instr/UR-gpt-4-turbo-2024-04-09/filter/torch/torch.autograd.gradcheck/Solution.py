import torch

def check_gradients(model, inputs, epsilon=1e-6):
    """
    Check gradients computed via small finite differences against
    analytical gradients with respect to tensors in inputs that
    are of floating point or complex type and have requires_grad=True.
    
    Args:
    - model: torch.nn.Module, model function which computes the output
    - inputs: list of Tensors, inputs to the model
    - epsilon: float, a small number to compute finite differences
    
    Returns:
    - Dictionary containing 'analytical_grad' and 'finite_diff_grad' for each input.
    """
    # Ensure model is in evaluation mode to avoid side effects from batch normalization or dropout
    model.eval()
    
    # Container to store gradients
    grad_check = {}
    
    for idx, input_tensor in enumerate(inputs):
        if input_tensor.dtype.is_floating_point or input_tensor.dtype.is_complex:
            if input_tensor.requires_grad:
                # Initialize gradient dictionaries
                grad_check[idx] = {'analytical_grad': [], 'finite_diff_grad': []}
                
                # Since the input_tensor needs to change, create a copy to modify
                input_tensor_perturbed = input_tensor.clone().detach()
                
                # Calculating the analytical gradients
                output = model(*inputs)
                output.backward()
                
                analytical_grad = input_tensor.grad
                
                # Calculating gradient using finite differences
                finite_diff_grad = torch.zeros_like(input_tensor)
                
                # Iterate over each element in the tensor
                for i in range(torch.numel(input_tensor)):
                    # Access the element index in the tensor
                    index = torch.tensor(i).unsqueeze(0)
                    idx_tuple = torch.unravel_index(index, input_tensor.shape)
                    
                    # Perturb the element positively
                    input_tensor_perturbed[idx_tuple] += epsilon
                    output_pos = model(*inputs)
                    
                    # Perturb the element negatively
                    input_tensor_perturbed[idx_tuple] -= 2 * epsilon
                    output_neg = model(*inputs)
                    
                    # Reset the perturbed tensor element
                    input_tensor_perturbed[idx_tuple] += epsilon
                    
                    # Calculate gradient approx
                    finite_diff = (output_pos - output_neg) / (2 * epsilon)
                    finite_diff_grad[idx_tuple] = finite_diff.detach()
                
                # save the results
                grad_check[idx]['analytical_grad'] = analytical_grad
                grad_check[idx]['finite_diff_grad'] = finite_diff_grad
        
    return grad_check
