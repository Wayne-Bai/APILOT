
import tensorflow as tf

# Input data
data = tf.placeholder(tf.float32, shape=(None, None))

# Segment IDs for each element in the input data
segment_ids = tf.placeholder(tf.int64, shape=(None, None))

# Compute the sum along segments of the input data
sess = tf.Session()
sums = sess.run(tf.math.segment_sum(data=data, segment_ids=segment_ids))
