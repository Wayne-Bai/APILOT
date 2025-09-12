
import tensorflow as tf
elems = [1, 2, 3, 4, 5, 6]
elems = tf.constant(elems)
def fn(x):
 return x + 10
elems_plus_10 = tf.map_fn(fn, elems)
with tf.Session() as sess:
 print(sess.run(elems_plus_10))
