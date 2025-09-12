import tensorflow as tf

def segment_sum(data, segment_ids):
    # Create a tensor to store the result
    result = tf.zeros_like(data, dtype=data.dtype)
    
    # Create a tensor to count the number of elements in each segment
    counts = tf.zeros_like(data, dtype=tf.int32)
    
    # Update the counts based on segment_ids
    unique_segment_ids, _ = tf.unique(segment_ids)
    counts = tf.tensor_scatter_nd_update(counts, tf.expand_dims(segment_ids, axis=1), tf.ones_like(segment_ids, dtype=tf.int32))
    
    # Sum the data based on segment_ids
    result = tf.tensor_scatter_nd_add(result, tf.expand_dims(segment_ids, axis=1), data)
    
    # Reduce the result to the number of unique segments
    result = tf.gather(result, unique_segment_ids)
    
    return result

# Example usage:
data = tf.constant([1, 2, 3, 4, 5, 6])
segment_ids = tf.constant([0, 0, 1, 1, 2, 2])
print(segment_sum(data, segment_ids))
