
import tensorflow as tf

raw_bytes = tf.placeholder(tf.string, shape=[None])

# Decode raw bytes into numeric tensors
decoded_tensors = tf.io.decode_raw(raw_bytes, out_type=tf.float32)

with tf.Session() as sess:
    numeric_tensors = sess.run(decoded_tensors, feed_dict={raw_bytes: your_raw_data})
