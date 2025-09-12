import tensorflow as tf

# Let's create some sample data
data = tf.constant([1, 2, 3, 4, 5, 6], dtype=tf.int32)
# Segment ids must be the same size as data and denote the segment each element belongs to
segment_ids = tf.constant([0, 0, 1, 1, 2, 2], dtype=tf.int32)

# Use tf.segment_sum to compute the sum along segments defined by segment_ids
segment_sums = tf.segment_sum(data, segment_ids)

# To see the result, we need to evaluate the tensor
print(segment_sums.numpy())
