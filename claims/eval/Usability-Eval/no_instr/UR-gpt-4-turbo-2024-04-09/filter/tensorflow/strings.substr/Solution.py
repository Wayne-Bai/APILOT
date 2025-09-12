import tensorflow as tf

# Create a Tensor of strings
tensor_of_strings = tf.constant(["Hello, TensorFlow!", "Welcome to the world of AI", "Deep Learning is fun!"])

# Define starting position and length for each substring extraction
start_position = 7
length = 10

# Extracting substrings
substrings = tf.strings.substr(tensor_of_strings, pos=start_position, len=length)

# To check the output
print(substrings)
