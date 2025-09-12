import torch

def compare_gradients(analytical_func, inputs, epsilon=1e-5, atol=1e-5):
    # Ensure inputs are tensors with requires_grad=True
    for tensor in inputs:
        assert tensor.requires_grad, "Input tensors must have requires_grad=True"
    
    # Compute analytical gradients
    analytical_outputs = analytical_func(*inputs)
    if isinstance(analytical_outputs, torch.Tensor):
        analytical_outputs = (analytical_outputs,)
    
    analytical_gradients = torch.autograd.grad(
        outputs=analytical_outputs, 
        inputs=inputs, 
        grad_outputs=[torch.ones_like(output) for output in analytical_outputs], 
        retain_graph=True,
        create_graph=True
    )
    
    # Compute finite difference gradients
    finite_difference_gradients = []
    for i, input_tensor in enumerate(inputs):
        finite_diff_grad = torch.zeros_like(input_tensor, dtype=torch.float32)
        
        # Iterate over each element in the input tensor
        for idx in range(input_tensor.numel()):
            # Create a view of the input tensor
            input_tensor_flat = input_tensor.view(-1)
            
            # Save original value
            original_val = input_tensor_flat[idx].item()
            
            # Calculate f(x + epsilon)
            input_tensor_flat[idx] = original_val + epsilon
            output_plus_epsilon = analytical_func(*inputs).sum()
            
            # Calculate f(x - epsilon)
            input_tensor_flat[idx] = original_val - epsilon
            output_minus_epsilon = analytical_func(*inputs).sum()
            
            # Reset to original value
            input_tensor_flat[idx] = original_val
            
            # Compute finite difference
            finite_diff_grad.view(-1)[idx] = (output_plus_epsilon - output_minus_epsilon) / (2 * epsilon)
        
        finite_difference_gradients.append(finite_diff_grad)

    # Compare gradients
    for i, (analytical, finite_diff) in enumerate(zip(analytical_gradients, finite_difference_gradients)):
        if not torch.allclose(analytical, finite_diff, atol=atol):
            print(f"Gradients do not match for input {i}:")
            print("Analytical:", analytical)
            print("Finite Difference:", finite_diff)
        else:
            print(f"Gradients match for input {i}.")
    
    return analytical_gradients, finite_difference_gradients

# Example use:
# Define a function for which you want to check gradients
def example_function(x, y):
    return x ** 2 + y ** 3

# Create input tensors with requires_grad=True
x = torch.tensor([1.0, 2.0], requires_grad=True)
y = torch.tensor([3.0, 4.0], requires_grad=True)

# Call the gradient comparison function
compare_gradients(example_function, [x, y])
