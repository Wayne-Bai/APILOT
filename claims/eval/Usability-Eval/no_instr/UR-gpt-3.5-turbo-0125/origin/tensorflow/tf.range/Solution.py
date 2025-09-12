
import tensorflow as tf

start = 1
stop = 10
step = 2

sequence = tf.range(start, stop, step, dtype=tf.int32)

with tf.Session() as sess:
    result = sess.run(sequence)

print(result)
