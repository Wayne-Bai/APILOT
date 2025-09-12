
import torch

def torch_linspace(start, end, steps):
    interval = (end - start) / (steps - 1)
    tensor = torch.arange(start, end+interval, interval)
    return tensor

start = 1
end = 10
steps = 5
result = torch_linspace(start, end, steps)
print(result)
