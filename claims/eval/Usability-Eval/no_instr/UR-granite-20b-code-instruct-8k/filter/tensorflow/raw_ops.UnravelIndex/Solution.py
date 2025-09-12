
import tensorflow as tf

indices = tf.constant([[0, 1], [1, 2]])

coordinates = tf.unravel_index(indices, (2, 3))

with tf.Session() as sess:
    print(sess.run(coordinates))
