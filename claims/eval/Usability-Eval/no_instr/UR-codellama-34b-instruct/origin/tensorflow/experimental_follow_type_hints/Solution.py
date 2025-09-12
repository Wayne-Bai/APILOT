import tensorflow as tf
from typing import Optional

@tf.function(autograph=True)
def my_func(x: tf.Tensor, y: tf.Tensor) -> tf.Tensor:
    return x + y

# This function will use the type annotations from `my_func` to optimize the tracing performance.
# The arguments annotated with `tf.Tensor` will automatically be converted to a Tensor.
def main():
    # Create some sample data
    x = tf.constant([[1, 2], [3, 4]])
    y = tf.constant([[5, 6], [7, 8]])

    # Call the function with the sample data
    result = my_func(x, y)

    print("Result:", result)
