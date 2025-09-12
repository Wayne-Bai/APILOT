import tensorflow as tf

def eager_execution_wrapper(func):
    def wrapper(*args, **kwargs):
        # Convert all TensorFlow tensors to eager tensors
        eager_args = [tf.convert_to_tensor(arg) for arg in args]
        eager_kwargs = {key: tf.convert_to_tensor(value) for key, value in kwargs.items()}
        
        # Execute the function eagerly
        result = func(*eager_args, **eager_kwargs)
        
        # Convert the result back to a TensorFlow tensor
        return tf.convert_to_tensor(result)
    
    return wrapper

# Example usage
@eager_execution_wrapper
def add_and_double(x, y):
    return (x + y) * 2

# Test the wrapped function
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])
result = add_and_double(a, b)
print(result.numpy())  # Output: [10 14 18]
