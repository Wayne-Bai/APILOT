import tensorflow as tf

@tf.function(experimental_autograph_options=tf.function.experimental.AutoGraphOptions(convert_by_default=True))
def my_func(x: tf.Tensor, y: tf.Tensor) -> tf.Tensor:
  return x + y
