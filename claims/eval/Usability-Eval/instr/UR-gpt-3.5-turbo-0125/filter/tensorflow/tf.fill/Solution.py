
import tensorflow as tf

scalar_value = 5
tensor = tf.fill([3, 3], scalar_value)

with tf.Session() as sess:
    result = sess.run(tensor)
    print(result)
