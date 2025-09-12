import tensorflow as tf
from tensorflow.experimental import dlpack

def tensor_to_dlpack(tensor):
    """
    Converts a TensorFlow tensor to a DLPack capsule.

    Args:
        tensor: A TensorFlow tensor.

    Returns:
        A DLPack capsule representing the tensor.
    """
    return dlpack.to_dlpack(tensor)

# Example usage:
tensor = tf.constant([1.0, 2.0, 3.0])
dlpack_capsule = tensor_to_dlpack(tensor)
print(dlpack_capsule)
