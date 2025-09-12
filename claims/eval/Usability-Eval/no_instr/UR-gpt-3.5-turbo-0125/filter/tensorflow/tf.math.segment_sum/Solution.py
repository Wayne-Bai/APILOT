
import tensorflow as tf

# Define a tensor
data = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the segmentation tensor
segment_ids = tf.constant([0, 0, 1])

# Computes the sum along segments of the tensor
result = tf.math.segment_sum(data, segment_ids)

print(result)
