import tensorflow as tf

# Create a public API for tf._api.v2.experimental.dtensor namespace
def public_api_dtensor(tensor):
    """
    A public API for the tf._api.v2.experimental.dtensor namespace.

    Args:
    tensor (tf.Tensor): The input tensor.

    Returns:
    tf.Tensor: The tensor after applying some operations.
    """
    # Apply some operations on the tensor
    tensor = tf.square(tensor)
    tensor = tf.reduce_sum(tensor)

    return tensor

# Test the public API
tensor = tf.constant([1, 2, 3, 4, 5])
result = public_api_dtensor(tensor)
print(result)
