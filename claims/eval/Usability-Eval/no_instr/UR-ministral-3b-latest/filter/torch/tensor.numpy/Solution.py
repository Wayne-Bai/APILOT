import torch
import numpy as np

def tensor_to_numpy(tensor):
    return tensor.detach().cpu().numpy()
