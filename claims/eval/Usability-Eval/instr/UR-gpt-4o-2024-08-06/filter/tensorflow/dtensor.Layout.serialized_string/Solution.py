import tensorflow as tf

# Create a TensorFlow constant
tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.int32)

# Convert the tensor to a TensorProto
tensor_proto = tf.make_tensor_proto(tensor)

# Serialize the TensorProto
serialized_tensor_proto = tensor_proto.SerializeToString()

# Print the serialized binary string representation
print(serialized_tensor_proto)
