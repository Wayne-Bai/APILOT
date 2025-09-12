import torch

# Define the parameters
base = 2 # The base of the logarithm
start = 1 # The starting value of the tensor
end = 16 # The ending value of the tensor
steps = 5 # The size of the tensor

# Create the tensor with logarithmically spaced values
tensor = torch.logspace(torch.log(torch.tensor(start)).log(base), torch.log(torch.tensor(end)).log(base), steps=steps, base=base)
