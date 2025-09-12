
import torch

steps = 10
start = 1
end = 100
base = 10

tensor = torch.logspace(start=start, end=end, steps=steps, base=base)
print(tensor)
