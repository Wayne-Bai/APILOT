import tensorflow as tf

# Define the input tensors
sorted_search_keys = tf.constant([[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]], dtype=tf.int32)
values = tf.constant([[0, 1, 5], [3, 6, 9]], dtype=tf.int32)

# Apply upper_bound using tf.raw_ops
upper_bound_indices = tf.raw_ops.UpperBound(sorted_inputs=sorted_search_keys, values=values)

# Evaluate the tensor
print('Upper Bound Indices:')
tf.print(upper_bound_indices)
