
import torch

# Define the tensor with requires_grad=True
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Define the function whose gradients we want to check
def func_to_check(x):
    return torch.sum(x**2)

# Compute the analytical gradients
func_to_check_result = func_to_check(x)
func_to_check_result.backward()

# Compute gradients via small finite differences
eps = 1e-6
finite_diff_grad = []
for i in range(len(x)):
    x_plus_eps = x.clone()
    x_plus_eps[i] += eps
    
    func_plus = func_to_check(x_plus_eps)
    func_minus = func_to_check(x)
    
    numerical_grad = (func_plus - func_minus) / eps
    finite_diff_grad.append(numerical_grad.item())

# Compare analytical gradients with numerical gradients
analytical_grad = x.grad.numpy().tolist()

print("Analytical Gradients:", analytical_grad)
print("Gradients via Finite Differences:", finite_diff_grad)
