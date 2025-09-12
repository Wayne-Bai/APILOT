import tensorflow as tf

def serialize_tensor(tensor):
    """
    Function to convert a TensorFlow tensor into a serialized Protobuf binary string representation.

    Args:
    tensor (tf.Tensor): Tensor to serialize.

    Returns:
    bytes: The serialized Protobuf binary string representation of the tensor.
    """
    # Make sure the tensor is in the default graph.
    tensor_proto = tf.make_tensor_proto(tensor)
    serialized_tensor = tensor_proto.SerializeToString()
    return serialized_tensor

# Example usage:
tensor = tf.constant([[1, 2], [3, 4]])
serialized_tensor = serialize_tensor(tensor)
print(serialized_tensor)
