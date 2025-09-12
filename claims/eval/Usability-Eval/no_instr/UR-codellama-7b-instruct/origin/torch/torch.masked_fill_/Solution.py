
# Define a function to fill elements of a tensor with a value based on a mask
def fill_tensor_mask(self, mask, value):
    # Ensure that the mask is broadcastable with the shape of the underlying tensor
    if not self.shape == mask.shape:
        raise ValueError("The shape of the mask must be broadcastable with the shape of the underlying tensor")

    # Create a tensor of zeros with the same shape as the underlying tensor
    zero_tensor = torch.zeros(self.shape)

    # Select elements from the zero tensor using the mask and set them to value
    return zero_tensor.scatter_(0, mask, value)
