import tensorflow as tf

def create_ones_tensor(input_tensor):
    """
    Creates a tensor of all ones that has the same shape as the input.

    Args:
    input_tensor (tf.Tensor): The input tensor whose shape will be used to create the ones tensor.

    Returns:
    tf.Tensor: A tensor of all ones with the same shape as the input tensor.
    """
    return tf.ones_like(input_tensor)
