import tensorflow as tf

# Define a tensor of ints
int_tensor = tf.constant([1, 2, 3, 4, 5])

# Create an encoding function to convert ints to unicode strings
# We need to know the characters to encode in advance
# For example, let's say we want to encode ints from 1 to 5 as '1', '2', '3', '4', '5'
encode_str = {v: str(v) for v in range(1, 6)}

# Encode the tensor of ints using the custom encoding function
encoded_str_tensor = tf.map_fn(lambda x: encode_str.get(x), int_tensor, dtype=tf.string)

print(encoded_str_tensor)  # Output: <tf.Tensor: shape=(5,), dtype=string>
