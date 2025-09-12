import torch

# Example tensors
input_tensor = torch.tensor([10, 20, 30, 40], dtype=torch.float32)
other_tensor = torch.tensor([2, 4, 5, 8], dtype=torch.float32)

# Element-wise division of input_tensor by other_tensor
result_tensor = torch.div(input_tensor, other_tensor)
print(result_tensor)
