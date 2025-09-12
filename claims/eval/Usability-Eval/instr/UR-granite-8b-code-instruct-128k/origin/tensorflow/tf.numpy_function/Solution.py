
import tensorflow as tf

def my_func(x):
  return x * x

my_op = tf.numpy_function(my_func, [tf.constant(2.0)], tf.float64)

with tf.Session() as sess:
  print(sess.run(my_op))
