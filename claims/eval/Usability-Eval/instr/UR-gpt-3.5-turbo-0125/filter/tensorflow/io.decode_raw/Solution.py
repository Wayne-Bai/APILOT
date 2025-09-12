
import tensorflow as tf

# Create a placeholder for raw bytes input tensor
raw_bytes_input = tf.placeholder(tf.string)

# Convert raw bytes tensor to numeric tensor
numeric_tensors = tf.io.decode_raw(raw_bytes_input, out_type=tf.float32)

# Sample usage to convert raw bytes into numeric tensors
with tf.Session() as sess:
    input_bytes = b'\x00\x00\x80?\x00\x00\x00@'
    numeric_values = sess.run(numeric_tensors, feed_dict={raw_bytes_input: input_bytes})
    print(numeric_values)
