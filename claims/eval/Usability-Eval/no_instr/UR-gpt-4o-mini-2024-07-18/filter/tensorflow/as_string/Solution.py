import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to strings using lower-level TensorFlow API
string_tensor = tf.strings.as_string(tensor)

# Print the resulting string tensor
tf.print(string_tensor)
