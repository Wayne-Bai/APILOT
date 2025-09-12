import tensorflow as tf

def wrap_python_function_as_tf_op(python_function):
    """Wraps a python function and uses it as a TensorFlow op.

    Args:
        python_function: The python function to be wrapped.

    Returns:
        A TensorFlow op that wraps the python function.
    """
    @tf.custom_op_impl
    def my_op_impl(context, *args):
        return python_function(*args)

    @tf.custom_op_grad
    def my_op_grad(op, grad):
        return grad

    return my_op_impl
