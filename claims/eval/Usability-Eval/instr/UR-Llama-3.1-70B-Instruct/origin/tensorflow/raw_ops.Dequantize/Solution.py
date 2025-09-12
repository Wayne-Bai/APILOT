# Import necessary libraries
import tensorflow as tf

# Define a function that dequantizes the input tensor
def dequantize_input(input_tensor, min_range, max_range, mode='min_combination'):
    """
    Dequantize the input tensor into a float or bfloat16 Tensor.

    Args:
    input_tensor: Input tensor to be dequantized.
    min_range: Minimum value of the input tensor range.
    max_range: Maximum value of the input tensor range.
    mode: Dequantization mode. Available modes are'min_combination','min_last','scott','sqrt','min_last plead'.

    Returns:
    Dequantized tensor.
    """
    # Dequantize the input tensor
    dequantized_tensor = tf.raw_ops.Dequantize(
        input=input_tensor,
        min_range=min_range,
        max_range=max_range,
        mode=mode
    )

    return dequantized_tensor

# Example usage:
if __name__ == "__main__":
    # Create an input tensor
    input_tensor = tf.constant([1, 2, 3, 4, 5])

    # Define the range of the input tensor
    min_range = 0
    max_range = 5

    # Dequantize the input tensor
    dequantized_tensor = dequantize_input(input_tensor, min_range, max_range)

    # Print the dequantized tensor
    print(dequantized_tensor)
