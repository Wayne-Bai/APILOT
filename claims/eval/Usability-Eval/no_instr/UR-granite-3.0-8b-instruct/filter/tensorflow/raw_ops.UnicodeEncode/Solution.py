import tensorflow as tf

# Assuming 'input_tensor' is your input tensor of ints
input_tensor = tf.constant([109, 111, 116, 105, 118, 97, 116, 105, 111, 110])

# Encode the tensor of ints into unicode strings
output_tensor = tf.raw_ops.EncodeUtf8(input_tensor)

# Print the output tensor
print(output_tensor)
