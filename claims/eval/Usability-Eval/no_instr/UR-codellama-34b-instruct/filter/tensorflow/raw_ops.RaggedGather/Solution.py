import tensorflow as tf

# Define a sample input and index tensor for gathering
input = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = tf.constant([[0], [1], [2]])

# Perform the gather operation using the `gather` method
output = tf.raw_ops.Gather(input, indices)

print("Output:", output)
