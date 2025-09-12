
import torch
from torch import nn

# Define a model with group norm
model = nn.Sequential(
    nn.Conv2d(3, 64, 3),
    nn.GroupNorm(num_groups=8, num_channels=64, affine=True),
    nn.ReLU(),
    nn.MaxPool2d(2, 2)
)

# Group norm with batch norm
model = nn.Sequential(
    nn.Conv2d(3, 64, 3),
    nn.GroupNorm(num_groups=8, num_channels=64, affine=True),
    nn.BatchNorm2d(64, affine=True),
    nn.ReLU(),
    nn.MaxPool2d(2, 2)
)

# Group norm with instance norm
model = nn.Sequential(
    nn.Conv2d(3, 64, 3),
    nn.GroupNorm(num_groups=8, num_channels=64, affine=True),
    nn.InstanceNorm2d(64, affine=True),
    nn.ReLU(),
    nn.MaxPool2d(2, 2)
)
