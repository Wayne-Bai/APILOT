
import tensorflow as tf

# Define the input tensors
sorted_search_values = tf.placeholder(tf.float32, shape=[None, None])
values = tf.placeholder(tf.float32, shape=[None, None])

# Apply upper_bound operation along each row
result = tf.raw_ops.UpperBound(sorted_search_values=sorted_search_values, values=values)

# Create a TensorFlow session and run the operation
with tf.Session() as sess:
    output = sess.run(result, feed_dict={sorted_search_values: your_sorted_search_values, values: your_values})
