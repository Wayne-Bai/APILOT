import tensorflow as tf
from tensorflow.python.ops.feature_column import make_feature_column
from tensorflow.python.ops.feature_column import make_parse_example_spec

# Input data
x1 = tf.placeholder(tf.float32, name='x1')
x2 = tf.placeholder(tf.float32, name='x2')

# Operation for calculating absolute difference
abs_diff = tf.abs(tf.subtract(x1, x2), name='abs_diff')

# Session
with tf.Session() as session:
    print("Absolute difference:", session.run(abs_diff, feed_dict={x1: 2, x2: 1}))
