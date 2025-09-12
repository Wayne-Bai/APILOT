import tensorflow as tf

# Assuming you have an input tensor of raw bytes
input_tensor = tf.constant(['01001100', '01001100', '01001100'])

# Use tf.decode_raw to convert raw bytes into numeric tensors
numeric_tensors = tf.decode_raw(input_tensor, tf.uint8)

with tf.Session() as sess:
    print(sess.run(numeric_tensors))
