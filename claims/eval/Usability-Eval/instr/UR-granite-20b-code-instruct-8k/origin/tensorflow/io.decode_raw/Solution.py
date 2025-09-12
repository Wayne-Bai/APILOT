import tensorflow as tf

# Define the input tensor
input_tensor = tf.convert_to_tensor([b'1.0', b'2.0', b'3.0'])

# Decode the raw bytes into numeric tensors
decoded_tensor = tf.io.decode_raw(input_tensor, out_type=tf.float32)

# Print the decoded tensor
print(decoded_tensor)
