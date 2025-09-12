import tensorflow as tf

def wrap_python_function_in_tf_op(python_function):
    """
    Wraps a python function into a TensorFlow op that executes it eagerly.

    Args:
    python_function: The python function to be wrapped.

    Returns:
    A TensorFlow op that executes the python function eagerly.
    """
    @tf.function
    def tf_op(*args, **kwargs):
        return python_function(*args, **kwargs)

    return tf_op
