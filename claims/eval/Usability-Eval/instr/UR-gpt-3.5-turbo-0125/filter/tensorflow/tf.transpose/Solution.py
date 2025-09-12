
import tensorflow as tf

# Create a placeholder Tensor
a = tf.placeholder(tf.float32, shape=[2, 3])

# Transpose the Tensor 'a'
transposed_a = tf.transpose(a)

# Print the transposed Tensor
with tf.Session() as sess:
    result = sess.run(transposed_a, feed_dict={a: [[1, 2, 3], [4, 5, 6]]})
    print(result)
