import tensorflow as tf
elems = tf.constant([1, 2, 3, 4, 5, 6])

def double(x):
 return x * 2

tf.map_fn(double, elems)
