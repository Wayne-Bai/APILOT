import torch
import torch.nn as nn
import torch.nn.functional as F

class RandomChannelZeroOut(nn.Module):
    def __init__(self, p):
        """
        Args:
            p (float): Probability to zero out a channel.
        """
        super(RandomChannelZeroOut, self).__init__()
        self.p = p

    def forward(self, x):
        # Sample a mask from a Bernoulli distribution
        mask = torch.bernoulli(torch.full_like(x[0, :, 0, 0], 1 - self.p))
        
        # Repeat the mask for all batches and for all spatial dimensions
        mask = mask.unsqueeze(0).unsqueeze(2).unsqueeze(3)
        
        # Apply the mask to the input
        return x * mask


# Example usage:
if __name__ == "__main__":
    # Initialize the module with a probability of 0.2
    rczo = RandomChannelZeroOut(p=0.2)
    
    # Create a random input
    input_tensor = torch.randn(1, 10, 32, 32)
    
    # Apply the RandomChannelZeroOut
    output = rczo(input_tensor)
    
    print("Input shape:", input_tensor.shape)
    print("Output shape:", output.shape)
    
    # Print the number of zeroed channels
    print("Number of zeroed channels:", (output[:, :, 0, 0] == 0).sum())
