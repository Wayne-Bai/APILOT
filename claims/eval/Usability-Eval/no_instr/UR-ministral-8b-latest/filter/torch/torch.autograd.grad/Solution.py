import torch

def sum_of_gradients(input_):
    # Define a dummy function to compute gradients of input_
    def dummy_function(x):
        return x.sum()

    # Forward backpropagation
    output = dummy_function(input_.clone())
    output.backward()

    # Sum the gradients
    sum_grad = input_.grad.sum()

    return sum_grad

# Example usage
input_tensor = torch.randn(3, 3, requires_grad=True)
result = sum_of_gradients(input_tensor)
print(result)  # This will print the sum of gradients
