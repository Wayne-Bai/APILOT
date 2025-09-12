import torch

class MaskedFiller(torch.autograd.Function):
    @staticmethod
    def forward(ctx, tensor, mask, value):
        """
        Fills elements of tensor with value where mask is True.
        
        Args:
            tensor (torch.Tensor): The tensor to modify.
            mask (torch.Tensor): A mask where True indicates the element in tensor should be modified.
            value (torch.Tensor or int): The value to fill the tensor with.
        
        Returns:
            torch.Tensor: A tensor with its elements filled based on the mask.
        """
        ctxtensor = tensor.detach()
        ctx.save_for_backward(mask)
        result = tensor.clone()
        result.masked_fill_(mask, value)
        return result

    @staticmethod
    def backward(ctx, grad_output):
        mask, = ctx.saved_tensors
        return grad_output.masked_fill_(~mask, 0), None, None

# Example usage
if __name__ == "__main__":
    # Initialize tensors
    tensor = torch.randn(3, 3)
    mask = torch.tensor([[True, False, True], [False, True, False], [True, False, True]])

    # Use the custom function to fill elements
    value = 10
    result = MaskedFiller.apply(tensor, mask, value)

    print("Original Tensor:")
    print(tensor)
    print("\nMask:")
    print(mask)
    print("\nFilled Tensor:")
    print(result)
