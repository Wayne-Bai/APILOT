import torch
import torch.nn as nn

class ChannelDropout(nn.Module):
    def __init__(self, p: float):
        """
        Randomly zero out entire channels with probability p.
        
        Args:
            p (float): Probability of zeroing out a channel.
        """
        super(ChannelDropout, self).__init__()
        if not 0 <= p <= 1:
            raise ValueError("p must be in the interval [0, 1].")
        self.p = p

    def forward(self, x):
        """
        Forward pass which randomly zeros out channels.
        
        Args:
            x (torch.Tensor): Input tensor with shape (N, C, H, W)
        
        Returns:
            torch.Tensor: Output tensor with channels randomly dropped out.
        """
        if not self.training or self.p == 0:
            return x
        
        # Create a mask using a Bernoulli distribution
        # The mask should have shape (N, C, 1, 1) to zero out complete channels
        probability = torch.empty(x.size(0), x.size(1), 1, 1, device=x.device).bernoulli_(1 - self.p)
        
        # Broadcast the mask over the other dimensions
        return x * probability

# Example usage
if __name__ == '__main__':
    # Define an input tensor with shape (batch_size=3, channels=5, height=4, width=4)
    x = torch.rand(3, 5, 4, 4)

    # Create a ChannelDropout layer with probability 0.5
    dropout_layer = ChannelDropout(p=0.5)
    
    # Set the layer into training mode
    dropout_layer.train()
    
    # Forward pass through the layer
    output = dropout_layer(x)
    print(output)
