import torch
import torch.nn as nn
import torch.nn.functional as F

class ClampValue(nn.Module):
    """
    Clamps all elements in input into the range [ min, max ].
    
    Parameters:
    - input: The input tensor to be clamped.
    - min: The minimum value to clamp to.
    - max: The maximum value to clamp to.
    
    Returns:
    - torch.Tensor: The clamped tensor.
    """

    def __init__(self, min, max):
        super(ClampValue, self).__init__()
        self.min = min
        self.max = max

    def forward(self, input):
        return torch.clamp(input, self.min, self.max)

# Example usage
if __name__ == "__main__":
    # Initialize device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Create a random tensor
    input_tensor = torch.randn(5, 5).to(device)
    print("Input Tensor:")
    print(input_tensor)

    # Clamp values between -10 and 10
    clamp_min = -10
    clamp_max = 10
    clamp_value = ClampValue(min=clamp_min, max=clamp_max)
    clamped_tensor = clamp_value(input_tensor)
    print("Clamped Tensor:")
    print(clamped_tensor)
