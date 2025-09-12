import torch

class MyTensor:
    def __init__(self, tensor):
        self.tensor = tensor

    def fill_mask(self, value, mask):
        self.tensor[mask] = value

# Example usage
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
mask = torch.tensor([[True, False], [False, True]])

mt = MyTensor(tensor)
mt.fill_mask(10.0, mask)
print(mt.tensor)
