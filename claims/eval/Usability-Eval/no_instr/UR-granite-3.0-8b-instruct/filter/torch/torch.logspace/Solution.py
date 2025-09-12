import torch

def create_log_spaced_tensor(base, start, end):
    return torch.logspace(torch.log(start) / torch.log(base), torch.log(end) / torch.log(base), steps)
