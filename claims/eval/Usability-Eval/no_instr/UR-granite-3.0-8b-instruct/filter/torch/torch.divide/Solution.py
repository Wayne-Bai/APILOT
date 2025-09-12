import torch

def divide_elements(input1, input2):
    # Check if inputs are tensors and have the same shape
    if not isinstance(input1, torch.Tensor) or not isinstance(input2, torch.Tensor) or input1.shape != input2.shape:
        raise ValueError("Inputs must be tensors with the same shape")

    # Perform element-wise division
    result = input1 / input2

    return result
