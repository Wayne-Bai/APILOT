import torch

def divide_elements(input, other):
    # Checking if sizes of inputs match
    assert input.size() == other.size(), "Input sizes do not match"

    # Using torch.div() to divide each element
    output = torch.div(input, other)

    return output
