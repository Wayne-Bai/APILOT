import tensorflow as tf

def serialize_protobuf(tensor):
    # Convert the tensor to a serialized Protobuf binary string
    serialized = tf.io.serialize_tensor(tensor)
    return serialized.numpy()

# Example usage:
tensor = tf.constant([1.0, 2.0, 3.0])
serialized_tensor = serialize_protobuf(tensor)
print(serialized_tensor)
