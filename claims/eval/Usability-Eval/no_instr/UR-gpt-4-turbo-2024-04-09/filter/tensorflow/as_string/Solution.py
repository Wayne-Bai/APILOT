import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4])

# Convert each entry in the tensor to strings
string_tensor = tf.strings.as_string(tensor)

print(string_tensor)
