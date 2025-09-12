import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1, 2, 3], dtype=tf.int32)

# Convert the input tensor to strings
output_tensor = tf.strings.as_string(input_tensor)

print(output_tensor)  # [b'1', b'2', b'3']
