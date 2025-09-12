import tensorflow as tf

a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
a_transposed = tf.transpose(a)

with tf.Session() as sess:
    print(sess.run(a_transposed))
