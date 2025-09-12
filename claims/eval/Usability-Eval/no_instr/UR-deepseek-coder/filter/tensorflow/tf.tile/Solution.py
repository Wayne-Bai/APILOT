import tensorflow as tf

def tile_tensor(input_tensor, multiples):
    """
    Constructs a tensor by tiling a given tensor.

    Args:
    input_tensor: The input tensor to be tiled.
    multiples: A list of integers specifying the number of repetitions for each dimension.

    Returns:
    A tensor that is the result of tiling the input tensor.
    """
    tiled_tensor = tf.tile(input_tensor, multiples)
    return tiled_tensor

# Example usage:
# input_tensor = tf.constant([[1, 2], [3, 4]])
# multiples = [2, 3]
# tiled_tensor = tile_tensor(input_tensor, multiples)
# print(tiled_tensor.numpy())
