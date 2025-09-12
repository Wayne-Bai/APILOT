import tensorflow as tf

@tf.function
def my_function(arg1: tf.Tensor, arg2: tf.Tensor) -> tf.Tensor:
    return arg1 + arg2
