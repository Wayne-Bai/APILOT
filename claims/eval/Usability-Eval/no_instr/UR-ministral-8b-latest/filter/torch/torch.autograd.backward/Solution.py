import torch

def compute_sum_of_gradients(tensors):
    sum_of_gradients = torch.sum(torch.autograd.grad(torch.zeros_like(tensors[0]), tensors, create_graph=True))
    return sum_of_gradients

# Example usage
input_tensor = torch.zeros((2, 3, 3))
output_tensor = input_tensor.sum(dim=1)
sum_of_grads = compute_sum_of_gradients([input_tensor, output_tensor])
print(sum_of_grads)
