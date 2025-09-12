import tensorflow as tf
import functools

# Define a decorator to wrap a function into a TensorFlow op
def eager_op(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        # Create a TensorFlow function to wrap the function
        tf_func = tf.function(lambda: func(*args, **kwargs))
        
        # Run the TensorFlow function eagerly
        return tf_func()
    return wrapped_func

# Example usage
@eager_op
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Outputs: 8
