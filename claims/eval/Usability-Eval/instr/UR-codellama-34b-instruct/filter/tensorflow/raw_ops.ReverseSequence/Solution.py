import tensorflow as tf

# Define a tensor with shape (3, 2)
tensor = tf.constant([[1, 2], [3, 4], [5, 6]])

# Reverse the tensor along the first dimension
reversed_tensor = tf.raw_ops.Reverse(tensor, [0])

print(reversed_tensor)  # prints [[5, 6], [3, 4], [1, 2]]
