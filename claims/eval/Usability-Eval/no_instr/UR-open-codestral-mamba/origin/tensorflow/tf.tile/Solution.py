import tensorflow as tf

def tile_tensor(t, multiples):
    """
    Tiles a tensor by replicating it on each dimension.

    Parameters:
    - t: Tensor
    - multiples: List of integers of the same length as t.shape

    Returns:
    - tiled tensor
    """
    return tf.tile(t, multiples)
