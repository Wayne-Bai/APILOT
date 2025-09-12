import torch

def create_log_spaced_tensor(start, end, steps, base):
    """
    Creates a one-dimensional tensor of size steps whose values are evenly spaced
    from start to end, inclusive, on a logarithmic scale with base base.
    """
    return torch.logspace(start=torch.log(start)/torch.log(base),
                          end=torch.log(end)/torch.log(base),
                          steps=steps, base=base)

# Usage
tensor = create_log_spaced_tensor(1, 10, 5, 2)
print(tensor)
