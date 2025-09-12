import torch

def elementwise_division(input, other):
    return input / other

# Example usage:
input_tensor = torch.tensor([10.0, 20.0, 30.0])
other_tensor = torch.tensor([2.0, 4.0, 5.0])

result = elementwise_division(input_tensor, other_tensor)
print(result)
