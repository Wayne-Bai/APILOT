import tensorflow as tf

numbers = tf.range(1, 10, dtype=tf.int32)

with tf.Session() as sess:
    print(sess.run(numbers))