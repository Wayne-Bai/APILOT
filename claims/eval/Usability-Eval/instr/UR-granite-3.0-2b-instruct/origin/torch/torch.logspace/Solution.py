import torch

def create_logarithmic_tensor(steps, start, end, base):
    tensor = torch.linspace(start, end, steps, device=torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    tensor = tensor * (base ** torch.linspace(0, 1, tensor.size(0)))
    return tensor
