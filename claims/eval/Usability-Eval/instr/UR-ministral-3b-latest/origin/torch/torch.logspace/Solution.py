import torch

def create_log_tensored(base, start, end, steps):
    return torch.linspace(start, end, steps, base=base)
