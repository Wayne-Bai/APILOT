import tensorflow as tf

# Define a simple feed and fetch
feed_dict = {
    'input_1': tf.constant([1.0, 2.0]),
    'input_2': tf.constant([3.0, 4.0])
}

output_tensor = tf.reduce_sum(feed_dict['input_1'] + feed_dict['input_2'])
