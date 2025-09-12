import tensorflow as tf

def eager_execution_wrapper(func):
    def wrapper(*args, **kwargs):
        # Convert input tensors to eager tensors if they are not already
        eager_args = [tf.convert_to_tensor(arg) if not isinstance(arg, tf.Tensor) else arg for arg in args]
        eager_kwargs = {key: tf.convert_to_tensor(value) if not isinstance(value, tf.Tensor) else value for key, value in kwargs.items()}
        
        # Execute the function eagerly
        result = func(*eager_args, **eager_kwargs)
        
        # Convert the result back to a TensorFlow tensor
        return tf.convert_to_tensor(result)
    
    return wrapper

# Example usage
@eager_execution_wrapper
def add_two_numbers(a, b):
    return a + b

# Test the wrapped function
a = tf.constant(3.0)
b = tf.constant(4.0)
result = add_two_numbers(a, b)
print(result.numpy())  # Output: 7.0
