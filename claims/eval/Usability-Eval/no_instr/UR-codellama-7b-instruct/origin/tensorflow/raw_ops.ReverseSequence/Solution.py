
import tensorflow as tf

def reverse_variable_length_slices(input_tensor, axis, input_length):
    """
    Reverses variable length slices of a tensor along a given axis.

    Args:
        input_tensor (tf.Tensor): The input tensor to be reversed.
        axis (int): The axis to reverse the slices along.
        input_length (tf.Tensor): The lengths of each slice in the input tensor.

    Returns:
        tf.Tensor: The reversed tensor with variable length slices.
    """
    # Check if input_length is a scalar or not
    if not tf.is_tensor(input_length):
        raise ValueError("Input 'input_length' must be a tensor.")

    # Create an empty tensor to store the output
    output_tensor = tf.empty_like(input_tensor)

    # Iterate over each slice in the input tensor
    for i in range(len(input_tensor)):
        # Get the current slice
        slice_tensor = input_tensor[i]

        # Get the length of the current slice
        slice_length = input_length[i]

        # Reverse the current slice and store it in the output tensor
        reversed_slice = tf.reverse(slice_tensor, axis)
        output_tensor[i] = reversed_slice[:slice_length]

    return output_tensor
