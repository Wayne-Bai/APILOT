import tensorflow as tf

# Create a tensor of strings
tensor = tf.constant(["Hello", "World", "TensorFlow", "Python"])

# Define a function to extract substrings
def extract_substrings(tensor, start, length):
    return tf.string.slice(tensor, start, length)

# Extract substrings from the tensor
substring_tensor = extract_substrings(tensor, 0, 5)

# Print the substring tensor
print(substring_tensor.numpy())
