import tensorflow as tf

# Let's assume we have a 2D tensor with shape (3, 4)
tensor = tf.constant([[3, 2, 4, 1], [5, 1, 3, 6], [8, 2, 5, 7]])

# Change this to the number of k largest entries you want to find
k = 3

# Use tf.nn.top_k to find the k largest entries, along the last axis
top_k, indices = tf.nn.top_k(tf.transpose(tensor, [1, 0])[:, ::-1], k)[-1]

# Swap axes back to the original order (shape: (4, 3))
indices = tf.transpose(indices[:, None], [1, 0])
top_k = tf.transpose(top_k[:, None], [1, 0])

print("Values of the k largest entries:", top_k)
print("Indices of the k largest entries:", indices)

# To access the actual values from the original tensor at the indices, you can do this
actual_values = tf.gather(tensor, indices[:, 0])
print("Actual values at the k largest indices:", actual_values)
