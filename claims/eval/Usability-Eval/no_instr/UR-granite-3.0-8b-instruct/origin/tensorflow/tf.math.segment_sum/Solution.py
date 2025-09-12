import tensorflow as tf

# Assuming you have a tensor `input_tensor` of shape (batch_size, num_segments, segment_length)
# and a tensor `segment_ids` of shape (batch_size, num_segments) where each row contains the segment ID for each segment in the corresponding row of `input_tensor`

# Compute the sum along segments of `input_tensor`
segment_sum = tf.math.segment_sum(input_tensor, segment_ids)
