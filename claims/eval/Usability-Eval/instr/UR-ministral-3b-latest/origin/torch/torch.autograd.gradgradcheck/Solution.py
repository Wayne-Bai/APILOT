import torch

# Example input tensors with requires_grad=True
input1 = torch.randn(5, requires_grad=True)
input2 = torch.randn(5, requires_grad=True)

# Example output tensor
output = torch.randn(5, requires_grad=True)

# Compute the analytical gradient of output wrt to input
analytical_grad = torch.autograd.grad(outputs=output,
                                    inputs=input1,
                                    grad_outputs=torch.ones(5), # Gradients of outputs

                                    only_inputs=True)  # Only compute numerical gradient

# Compute the gradient via small finite differences
finite_diff_grad = torch.autograd.grad(outputs=output,
                                    inputs=input1,
                                    grad_outputs=input1.new(dtype=torch.float),
                                    create_graph=True)  # Create a computational graph

# The function call by grad returns a tuple with: grad of 'output' wrt 'input1' + grad of 'output' wrt 'output' wrt 'input1'
print("Analytical Gradient :", analytical_grad)
print("Finite Difference Gradient :", finite_diff_grad)

# Now compute gradient wrt another input
analytical_grad2 = torch.autograd.grad(outputs=output,
                                    inputs=input2,
                                    grad_outputs=input2.new(dtype=torch.float),
                                    only_inputs=False)
print("Second Analytical Gradient :", analytical_grad2)

