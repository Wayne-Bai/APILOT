import tensorflow as tf

def serialize_tensor(tensor):
    """Serializes a TensorFlow tensor to a Protobuf binary string representation."""
    # Use TensorProto for serialization
    tensor_proto = tf.make_tensor_proto(tensor)
    return tensor_proto.SerializeToString()

# Example usage
if __name__ == "__main__":
    # Create a sample tensor
    sample_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
    
    # Serialize the tensor
    serialized_tensor = serialize_tensor(sample_tensor)
    print(serialized_tensor)
