import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Define a function to convert each element to string
def string_conversion(x):
    return tf.strings.as_utf8(tf.strings.as_bytes(x))

# Use vectorized map to apply the function
string_tensor = tf.vectorized_map(string_conversion, tensor)

# To print the result
print(tf.strings.as_utf8([string_tensor]))
