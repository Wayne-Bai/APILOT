import tensorflow as tf

# Create a simple constant tensor
const_tensor = tf.constant([1.0, 2.0, 3.0])

# Get the underlying representation as a Dlpack tensor
dlpack_tensor = tf.dlpack.convert_to_dlpack(const_tensor)

# Print the tensor data
print(dlpack_tensor)
