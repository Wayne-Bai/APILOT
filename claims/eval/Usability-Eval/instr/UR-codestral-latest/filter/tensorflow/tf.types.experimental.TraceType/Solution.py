import tensorflow as tf

@tf.function(input_signature=[tf.TensorSpec(shape=None, dtype=tf.float32)])
def my_function(x):
  return tf.square(x)
