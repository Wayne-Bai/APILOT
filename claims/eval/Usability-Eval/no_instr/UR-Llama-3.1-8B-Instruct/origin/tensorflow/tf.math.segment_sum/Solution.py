# Import necessary libraries
import tensorflow as tf
import numpy as np

# Define a function to compute the sum along segments of a tensor
def compute_segment_sum(input_tensor, segment_ids, num_segments):
    """
    Compute the sum along segments of a tensor.

    Args:
    input_tensor: The input tensor.
    segment_ids: A 1-D tensor containing segment indices of the input tensor.
    num_segments: The number of segments in the input tensor.

    Returns:
    A tensor containing the sum of each segment in the input tensor.
    """
    return tf.math.segment_sum(input_tensor, tf.cast(segment_ids, tf.int64), num_segments=num_segments)


# Generate sample input data
input_tensor = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9])
segment_ids = tf.constant([0, 0, 1, 1, 2, 2, 3, 3, 3])

# Compute the sum along segments
segment_sum = compute_segment_sum(input_tensor, segment_ids, tf.size(segment_ids).numpy())

# Print the result
print("Input Tensor: ", input_tensor.numpy())
print("Segment IDs: ", segment_ids.numpy())
print("Segment Sum: ", segment_sum.numpy())
