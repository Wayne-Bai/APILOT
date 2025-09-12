import tensorflow as tf

def tile_tensor(tensor, multiple, axis):
    """
    Tiles a given tensor along a specified axis.

    Parameters:
    tensor (tf.Tensor): The input tensor to be tiled.
    multiple (int): The number of times to tile the tensor.
    axis (int): The axis along which the tensor should be tiled.

    Returns:
    tf.Tensor: The tiled tensor.
    """
    # Use tf.tile to tile the tensor
    tiled_tensor = tf.tile(tensor, [1] * (tf.range(multiple).numpy(),) + [multiple])
    return tiled_tensor

# Example usage:
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
tiled_tensor = tile_tensor(input_tensor, 3, axis=0)
print(tiled_tensor)
