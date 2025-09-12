import tensorflow as tf
from tensorflow.types import ExperimentalAutographAllowed

def optimize_tracing(func):
    """
    Function decorator to optimize tracing performance.
    
    When True, the function may use type annotations from `func` to optimize the tracing performance.
    For example, arguments annotated with `tf.Tensor` will automatically be converted to a Tensor.

    Args:
        func: Function to optimize.

    Returns:
        Optimized function.
    """
    @ExperimentalAutographAllowed
    def wrapper(*args, **kwargs):
        args = list(args)
        for i, arg in enumerate(args):
            if func.__annotations__.get('arg' + str(i)) == tf.Tensor:
                args[i] = tf.convert_to_tensor(arg)
        for key, value in kwargs.items():
            if key in func.__annotations__ and func.__annotations__[key] == tf.Tensor:
                kwargs[key] = tf.convert_to_tensor(value)
        return func(*args, **kwargs)
    return wrapper


# Example usage
@optimize_tracing
def add(a: tf.Tensor, b: tf.Tensor) -> tf.Tensor:
    """
    Add two tensors.

    Args:
        a: First tensor.
        b: Second tensor.

    Returns:
        Sum of the two tensors.
    """
    return tf.add(a, b)


# Test the function
result = add(2, 3)
print(result)  # Output: tf.Tensor(5, shape=(), dtype=int32)
result = add(tf.constant(2), tf.constant(3))
print(result)  # Output: tf.Tensor(5, shape=(), dtype=int32)
