import tensorflow as tf

# Create a tensor variable
x = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=tf.int64)

# Create a tensor containing indices
indices = tf.constant([1, 2], dtype=tf.int32)

# Use tf.gather function to gather slices from tensor x
result = tf.gather(x, indices)

# Start a new tensorflow session
with tf.compat.v1.Session() as sess:
  # Print the result
  print(result.eval())
