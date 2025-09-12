import tensorflow as tf
import numpy as np

def segment_sum(tensor, num_segments):
    """
    Computes the sum along segments of a tensor.

    Args:
    tensor: The input tensor.
    num_segments: The number of segments.

    Returns:
    The sum of each segment.
    """
    
    # Split the tensor along the 0th axis (which would be the rows in a 2D tensor)
    # into as many segments as specified
    segs = tf.data.Dataset.from_tensor_slices(tensor).batch(num_segments)
    
    # Use a loop to add up the elements in each segment
    seg_sums = []
    for i, seg in enumerate(segs):
        seg_sums.append(tf.reduce_sum(seg))
    
    # Stack the segment sums into a tensor
    seg_sum = tf.convert_to_tensor(seg_sums)
    
    return seg_sum

# Example usage
tensor = tf.constant([1, 2, 3, 4, 5, 6], shape=[1, 6])
num_segments = 3

result = segment_sum(tensor, num_segments)
print(result)
