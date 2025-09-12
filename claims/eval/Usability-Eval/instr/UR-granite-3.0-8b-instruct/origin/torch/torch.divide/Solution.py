import torch

def divide_tensors(input1, input2):
    # Check if the tensors have the same shape
    assert input1.shape == input2.shape, "Input tensors must have the same shape"

    # Perform element-wise division
    result = input1 / input2

    return result
