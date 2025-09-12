import torch

class TensorFiller:
    def fill_where_mask(self, tensor, mask, fill_value):
        """
        Fills elements of the tensor with the fill_value where the mask is True.

        The shape of the mask must be broadcastable with the shape of the underlying tensor.

        Parameters:
        tensor (tensor): Input tensor to be filled.
        mask (tensor): Mask to determine which elements to fill in the tensor.
        fill_value (scalar): Value to fill in the tensor where the mask is True.

        Returns:
        tensor: The filled tensor.
        """
        return torch.where(mask, fill_value, tensor)

# Example usage
if __name__ == "__main__":
    # Create a tensor
    tensor = torch.ones(3, 3)
    print("Original Tensor:")
    print(tensor)

    # Create a mask tensor
    mask = torch.tensor([[True, False, True], [False, True, False], [True, False, True]])
    print("\nMask Tensor:")
    print(mask)

    # Fill the tensor where the mask is True
    fill_value = 5.0
    filled_tensor = TensorFiller().fill_where_mask(tensor, mask, fill_value)
    print("\nFilled Tensor:")
    print(filled_tensor)
