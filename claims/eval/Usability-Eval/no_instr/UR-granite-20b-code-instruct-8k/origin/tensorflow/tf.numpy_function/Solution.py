import tensorflow as tf

def my_func(x):
    return x * x

tf_func = tf.py_function(my_func, [tf.TensorSpec([], tf.float32)], tf.float32)
