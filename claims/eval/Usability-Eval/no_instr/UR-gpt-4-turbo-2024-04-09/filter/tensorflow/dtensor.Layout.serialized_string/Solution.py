import tensorflow as tf

# Create a Tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Convert tensor to a TensorProto object
tensor_proto = tf.make_tensor_proto(tensor)

# Serialize the TensorProto object to a binary string
serialized_tensor = tensor_proto.SerializeToString()

print(serialized_tensor)
