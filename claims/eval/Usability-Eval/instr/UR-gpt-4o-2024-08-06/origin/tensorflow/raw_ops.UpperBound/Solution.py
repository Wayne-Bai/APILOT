import tensorflow as tf

# Create a 2D tensor for sorted values along each row
sorted_search_values = tf.constant([[1, 2, 4, 6], [0, 3, 5, 7]], dtype=tf.int32)

# Create a 2D tensor for values to locate
values = tf.constant([[2, 3, 5], [1, 6, 8]], dtype=tf.int32)

# Since the UpperBound is an outdated API, we can replicate the functionality using different means.
# We can simulate the 'upper_bound' functionality using tf.searchsorted in "right" mode.

upper_bound_indices = tf.searchsorted(sorted_search_values, values, side='right')

# Start a session to evaluate and print the result if using TensorFlow 1.x
# With TensorFlow 2.x (eager execution enabled by default), directly evaluate in Python
print("Upper Bound Indices:\n", upper_bound_indices.numpy())
