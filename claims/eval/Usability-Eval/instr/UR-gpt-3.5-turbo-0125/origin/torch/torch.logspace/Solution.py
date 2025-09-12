
import torch

base = 10.0
start = 1.0
end = 100.0
steps = 10

logspace_tensor = torch.logspace(start=torch.log10(start)/torch.log10(base), end=torch.log10(end)/torch.log10(base), steps=steps, base=base)
print(logspace_tensor)
