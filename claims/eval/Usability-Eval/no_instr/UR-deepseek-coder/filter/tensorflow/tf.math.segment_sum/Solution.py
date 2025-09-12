import tensorflow as tf

def segment_sum(data, segment_ids):
    # Ensure segment_ids is a Tensor
    segment_ids = tf.convert_to_tensor(segment_ids)
    
    # Get unique segment IDs and their corresponding indices
    unique_segment_ids, new_segment_ids = tf.unique(segment_ids)
    
    # Gather data based on the new segment IDs
    gathered_data = tf.gather(data, new_segment_ids)
    
    # Reduce sum along the gathered data
    summed_data = tf.math.segment_sum(gathered_data, tf.range(tf.shape(unique_segment_ids)[0]))
    
    return summed_data

# Example usage:
data = tf.constant([1, 2, 3, 4, 5, 6])
segment_ids = tf.constant([0, 0, 1, 1, 2, 2])
result = segment_sum(data, segment_ids)
print(result.numpy())  # Output should be [3, 7, 11]
