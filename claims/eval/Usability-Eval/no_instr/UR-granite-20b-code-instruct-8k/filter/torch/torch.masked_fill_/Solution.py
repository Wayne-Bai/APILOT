
import torch

def fill_where(self, mask, value):
    return self.masked_fill(mask, value)
