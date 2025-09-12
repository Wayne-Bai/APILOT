import torch

def group_norm(input, num_groups, num_channels, eps=1e-5):
    """
    Applies Group Normalization over a mini-batch of inputs.

    Args:
        input (torch.Tensor): Input tensor of shape (batch, num_channels, *)
        num_groups (int): Number of groups to separate the channels into
        num_channels (int): Number of channels in the input tensor
        eps (float, optional): Small constant to avoid divide-by-zero errors. Default: 1e-5

    Returns:
        torch.Tensor: The normalized tensor of the same shape as the input tensor
    """
    assert input.dim() >= 3, "Expected input tensor to be at least 3-dimensional (shape: (batch, num_channels, *))"

    # Reshape the input tensor into a (batch, num_groups, num_channels_per_group, *) shape
    shape = (input.shape[0], num_groups, -1) + input.shape[2:]
    input = input.view(shape)

    # Calculate the mean and standard deviation of the input tensor within each group
    mean = input.mean(dim=2, keepdim=True)
    std = input.std(dim=2, keepdim=True)

    # Normalize the input tensor
    output = (input - mean) / (std + eps)

    # Restore the original shape of the input tensor
    output = output.view(input.shape)

    return output