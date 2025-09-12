
import tensorflow as tf

# Define a sample tensor
tensor = tf.constant([1.5, 2.3, 3.7, 4.2])

# Convert each entry in the tensor to strings
tensor_strings = tf.strings.as_string(tensor)

# Display the converted tensor
print(tensor_strings)
