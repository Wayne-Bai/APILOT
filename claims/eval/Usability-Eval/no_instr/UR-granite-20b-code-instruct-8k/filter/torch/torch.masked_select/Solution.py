
import torch

def index_select_1d(input, mask):
    return torch.index_select(input, 0, mask)
