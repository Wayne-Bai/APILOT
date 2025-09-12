import tensorflow as tf

# Creating some sample data and 'pred'
data = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
pred = tf.constant([1, 0])  # You can replace this with your own pred

# Creating two output tensors to which data will be forwarded based on 'pred'
output_true = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)
output_false = tf.constant([[9, 10], [11, 12]], dtype=tf.float32)

# Using tf.raw_ops.Switch to forward data to the output port determined by 'pred'
output = tf.raw_ops.Switch(data=data, pred=pred, true=output_true, false=output_false)

with tf.Session() as sess:
    result = sess.run(output)
    print(result)
