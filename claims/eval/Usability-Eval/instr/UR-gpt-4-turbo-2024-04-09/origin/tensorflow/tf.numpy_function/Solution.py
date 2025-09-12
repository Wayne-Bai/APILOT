import tensorflow as tf

def py_func(func, inp, Tout, stateful=True, name=None):
    """
    This function wraps a python function and uses it as a TensorFlow op.

    Args:
        func: Python function to be used as a TensorFlow op.
        inp: List of inputs to the function.
        Tout: Output type(s) of the function.
        stateful: Whether the function should be considered stateful. Default is True.
        name: Optional name for the operation.

    Returns:
        A TensorFlow tensor or a list of tensors, which are the output of the Python function.
    """
    placeholder_name = f"PyFunc_{name}" if name else "PyFunc"
    return tf.numpy_function(func, inp, Tout, stateful, name=placeholder_name)

# Example usage of the wrapped function
def multiply_by_two(x):
    return x * 2

# Input tensor
input_tensor = tf.constant([1, 2, 3, 4])

# Use the `py_func` to wrap the Python function as a TensorFlow operation
result_tensor = py_func(multiply_by_two, [input_tensor], tf.int32)

# Evaluate the result
print("Output after multiply_by_two:", result_tensor.numpy())  # Make sure running in an environment where .numpy() can be called
