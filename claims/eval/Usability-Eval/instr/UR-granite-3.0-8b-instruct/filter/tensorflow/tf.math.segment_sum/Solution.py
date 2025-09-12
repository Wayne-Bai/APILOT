import tensorflow as tf

# Assuming 'data' is your input tensor and 'segment_ids' is the tensor containing segment ids
# 'num_segments' is the number of distinct segment ids

# Compute the sum along segments
segment_sums = tf.math.segment_sum(data, segment_ids, num_segments)
