import tensorflow as tf
elems = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
def fn(x):
 return x * x
elems_times_2 = tf.map_fn(fn, elems, dtype=tf.int32)
