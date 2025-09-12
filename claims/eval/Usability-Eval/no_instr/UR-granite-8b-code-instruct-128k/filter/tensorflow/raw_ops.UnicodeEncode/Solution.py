import tensorflow as tf

# Create a tensor of ints
tensor = tf.constant([1, 2, 3], dtype=tf.int32)

# Encode the tensor into unicode strings
encoded_strings = tf.as_string(tensor)

# Print the encoded strings
print(encoded_strings.numpy())
