import tensorflow as tf

# Create sample tensors
dtype = tf.resource
input_tensor = tf.constant([1, 2, 3], dtype=dtype)
bias_tensor = tf.constant([4, 5, 6], dtype=dtype)

# Create a Quantized type (Let's use Int32 quantized to example)
quantized_input = tf.cast(input_tensor, dtype=tf.int32)
quantized_bias = tf.cast(bias_tensor, dtype=tf.int32)

# Use tf.raw_ops BiasAdd function to add bias to input for Quantized types
# Note: This function is part of the tf.raw_ops module, which is for low-level operations.
bias_add = tf.raw_ops.BiasAdd(input=quantized_input, bias=quantized_bias, data_format=None)

# Print the output
print(bias_add)
