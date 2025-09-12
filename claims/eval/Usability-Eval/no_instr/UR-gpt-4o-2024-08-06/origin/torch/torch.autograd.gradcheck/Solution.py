import torch

def check_gradients(analytical_func, inputs, epsilon=1e-6, atol=1e-4, rtol=1e-4):
    assert isinstance(inputs, (list, tuple)), "inputs should be a list or tuple of Tensors"
    
    # Ensure all input tensors have requires_grad=True
    for tensor in inputs:
        assert tensor.requires_grad, "All input tensors must have requires_grad=True"

    # Evaluate analytical gradients
    analytical_outputs = analytical_func(*inputs)
    if torch.is_tensor(analytical_outputs):
        analytical_outputs = (analytical_outputs,)
    analytical_grads = torch.autograd.grad(analytical_outputs, inputs, grad_outputs=torch.ones_like(analytical_outputs[0]))

    # Evaluate numerical gradients using finite differences
    numerical_grads = []
    for i, tensor in enumerate(inputs):
        numerical_grad = torch.zeros_like(tensor)
        tensor_data = tensor.data
        
        for idx in torch.ndindex(tensor_data.shape):
            orig_value = tensor_data[idx].item()
            
            # f(x + epsilon)
            tensor_data[idx] = orig_value + epsilon
            positive_outputs = analytical_func(*inputs)
            positive_outputs = positive_outputs[0] if len(positive_outputs) == 1 else sum(positive_outputs)
            
            # f(x - epsilon)
            tensor_data[idx] = orig_value - epsilon
            negative_outputs = analytical_func(*inputs)
            negative_outputs = negative_outputs[0] if len(negative_outputs) == 1 else sum(negative_outputs)
            
            # Reset original value
            tensor_data[idx] = orig_value
            
            # Compute numerical gradient
            numerical_grad[idx] = (positive_outputs - negative_outputs) / (2 * epsilon)
        
        numerical_grads.append(numerical_grad)

    # Compare analytical and numerical gradients
    for i, (analytical, numerical) in enumerate(zip(analytical_grads, numerical_grads)):
        if not torch.allclose(analytical, numerical, atol=atol, rtol=rtol):
            print(f"Mismatch found in gradient for input {i}!")
            print(f"Analytical Gradient: {analytical}")
            print(f"Numerical Gradient: {numerical}")
        else:
            print(f"Gradients match for input {i}.")

# Example Usage
def example_function(x, y):
    return x * y + torch.cos(x)

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = torch.tensor([4.0, 5.0, 6.0], requires_grad=True)

check_gradients(example_function, [x, y])
