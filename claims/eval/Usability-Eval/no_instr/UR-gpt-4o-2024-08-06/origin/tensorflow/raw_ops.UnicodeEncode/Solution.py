import tensorflow as tf

# Define the input tensor, which is a tensor of integers
input_tensor = tf.constant([72, 101, 108, 108, 111], dtype=tf.int32)  # Example for string 'Hello'

# Encode the input tensor of integers into unicode strings using tf.strings.unicode_encode
output_tensor = tf.strings.unicode_encode(input_tensor, output_encoding='UTF-8')

# Execute the TensorFlow graph and evaluate the output tensor
result = tf.keras.backend.get_value(output_tensor)

# Print the result
print(result)
