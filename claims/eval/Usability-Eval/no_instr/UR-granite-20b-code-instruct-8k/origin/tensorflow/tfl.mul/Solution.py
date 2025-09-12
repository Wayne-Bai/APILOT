import tensorflow as tf
a = tf.constant([2,3], name='a')
b = tf.constant([4,5], name='b')
c = tf.multiply(a, b, name='c')
with tf.Session() as sess:
    print(sess.run(c))
