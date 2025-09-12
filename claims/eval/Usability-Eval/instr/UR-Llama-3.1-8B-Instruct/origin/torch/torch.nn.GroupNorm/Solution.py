import torch
import torch.nn as nn
import math

# Function to calculate the mean and std of each group separately
def group_norm_forward(input, group, num_features):
    B, C, H, W = input.shape
    group_shape = (B, group, math.ceil(C / group), H, W)
    input_split = input.view(group_shape)
    mean = input_split.mean(dim=2, keepdim=True)
    variance = (input.split(group) ** 2).mean(dim=2, keepdim=True)

    return torch.zeros(B, C, H, W).type_as(input), variance

# Function to apply Group Normalization
class GroupNorm(nn.Module):
    def __init__(self, num_features, num_groups=2):
        super(GroupNorm, self).__init__()
        self.num_features = num_features
        self.num_groups = num_groups

    def forward(self, input):
        var, norm_input = group_norm_forward(input, self.num_groups, self.num_features)
        norm_input = norm_input.sqrt()

        return input / norm_input
