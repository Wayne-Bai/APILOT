
import tensorflow as tf

seq = tf.range(10)

with tf.Session() as sess:
    result = sess.run(seq)

print(result)
