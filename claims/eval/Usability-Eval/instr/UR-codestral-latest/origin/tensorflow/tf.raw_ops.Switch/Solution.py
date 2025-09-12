import tensorflow as tf

# Assuming you have a tensor of data and a tensor of indices
data = tf.constant([[1, 2], [3, 4], [5, 6]])
pred = tf.constant([[0, 1], [1, 0]])  # These indices would select [1, 4]

# Convert indices to int64 for tf.gather_nd
pred = tf.cast(pred, tf.int64)

# Add a new axis to the pred tensor so it matches the rank of the data tensor
indices = tf.expand_dims(pred, axis=-1)

# Use tf.gather_nd to select elements from the data tensor based on the indices
output = tf.gather_nd(data, indices)

# Run the graph
with tf.Session() as sess:
    output_value = sess.run(output)
    print(output_value)
