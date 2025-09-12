import torch
import torch.nn as nn
import torch.nn.functional as F

class RandomChannelDropout(nn.Module):
    """
    Randomly zero out entire channels (a channel is a 2D feature map).
    Each channel will be zeroed out independently on every forward call with probability p.
    """
    def __init__(self, p=0.5):
        """
        Args:
            p (float, optional): probability of an channel to be zeroed. Defaults to 0.5.
        """
        super(RandomChannelDropout, self).__init__()
        self.p = p

    def forward(self, x):
        """
        Args:
            x (torch.Tensor): input tensor with shape (N, C, H, W)

        Returns:
            torch.Tensor: output tensor with shape (N, C, H, W)
        """
        if self.training:
            # Generate a mask for each channel
            mask = torch.bernoulli(torch.full((1, x.size(1), 1, 1), 1 - self.p, device=x.device))
            return mask * x
        else:
            return x

# Usage
if __name__ == "__main__":
    # Set the seed for reproducibility
    torch.manual_seed(123)

    # Create an instance of RandomChannelDropout
    dropout = RandomChannelDropout(p=0.2)

    # Create a dummy input tensor
    input_tensor = torch.randn(1, 10, 5, 5)

    # Call the forward pass
    output_tensor = dropout(input_tensor)

    print("Input Tensor Shape:", input_tensor.shape)
    print("Output Tensor Shape:", output_tensor.shape)
