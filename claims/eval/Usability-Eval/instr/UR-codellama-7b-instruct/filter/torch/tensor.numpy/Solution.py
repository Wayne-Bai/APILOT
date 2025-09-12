import torch

def tensor_to_numpy(tensor):
    return tensor.detach().cpu().numpy()