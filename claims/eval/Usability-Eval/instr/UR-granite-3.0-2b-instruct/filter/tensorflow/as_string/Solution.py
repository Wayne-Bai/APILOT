import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to strings
tensor_str = tf.string_join([tf.strings.as_string(x) for x in tensor.numpy().tolist()], ', ')

# Print the result
print(tensor_str)
