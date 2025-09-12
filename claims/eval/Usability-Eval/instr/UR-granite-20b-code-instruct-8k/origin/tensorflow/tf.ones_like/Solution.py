import tensorflow as tf

def create_ones_tensor(input_tensor):
    """
    Creates a tensor of all ones that has the same shape as the input.
    Args:
    input_tensor: The input tensor whose shape will be used to define the shape of the output tensor.
    Returns:
    A tensor of all ones with the same shape as the input tensor.
    """
    ones_tensor = tf.ones_like(input_tensor)
    return ones_tensor
