import tensorflow as tf

def tile_tensor(input_tensor, multiples):
    """
    Constructs a tensor by tiling a given tensor.

    Parameters:
        input_tensor (tf.Tensor): The tensor to tile.
        multiples (list of int): How many times the tensor should be tiled in each dimension.

    Returns:
        tf.Tensor: The tiled tensor.
    """
    tiled_tensor = tf.tile(input_tensor, multiples)
    return tiled_tensor

# Example usage
input_tensor = tf.constant([[1, 2], [3, 4]])
multiples = [2, 3]
result_tensor = tile_tensor(input_tensor, multiples)
print(result_tensor)
