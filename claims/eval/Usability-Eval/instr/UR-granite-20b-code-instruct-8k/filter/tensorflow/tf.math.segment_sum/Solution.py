
import tensorflow as tf

# Assuming 'data' is your tensor and 'segment_ids' is the tensor containing the segment IDs
output = tf.math.segment_sum(data, segment_ids)
