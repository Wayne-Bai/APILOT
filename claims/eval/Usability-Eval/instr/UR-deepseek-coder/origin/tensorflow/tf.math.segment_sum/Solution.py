import tensorflow as tf

def segment_sum(data, segment_ids):
    # Ensure segment_ids is a 1D tensor
    segment_ids = tf.convert_to_tensor(segment_ids)
    
    # Sort data and segment_ids by segment_ids
    sorted_indices = tf.argsort(segment_ids)
    sorted_data = tf.gather(data, sorted_indices)
    sorted_segment_ids = tf.gather(segment_ids, sorted_indices)
    
    # Find unique segment ids and their counts
    unique_segment_ids, _, counts = tf.unique_with_counts(sorted_segment_ids)
    
    # Split data based on counts
    split_data = tf.split(sorted_data, counts)
    
    # Sum each segment
    segment_sums = tf.stack([tf.reduce_sum(segment, axis=0) for segment in split_data])
    
    return segment_sums

# Example usage:
data = tf.constant([1, 2, 3, 4, 5, 6])
segment_ids = tf.constant([0, 0, 1, 1, 2, 2])
result = segment_sum(data, segment_ids)
print(result.numpy())  # Output: [3 7 11]
