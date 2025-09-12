import tensorflow as tf

def annotated_function(x: tf.Tensor) -> tf.Tensor:
    # Your function implementation here
    pass

# To use type annotations for tracing performance optimization
# When True, the function may use type annotations from `func` to optimize the tracing performance.
# For example, arguments annotated with `tf.Tensor` will automatically be converted to a Tensor.
tf.debugging.assert_type(x, tf.Tensor, message="x must be a Tensor")
