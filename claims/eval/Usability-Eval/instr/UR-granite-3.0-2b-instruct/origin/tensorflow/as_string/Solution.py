import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to strings
tensor_str = tf.string_reshape(tf.string_annotate(tensor), [-1, 1])

# Print the resulting tensor
print(tensor_str)
