import tensorflow as tf

@tf.function(jit_compile=True)
def my_function(x: tf.Tensor, y: tf.Tensor) -> tf.Tensor:
    return x + y
