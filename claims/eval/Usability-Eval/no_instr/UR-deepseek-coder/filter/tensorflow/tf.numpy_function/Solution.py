import tensorflow as tf

def py_function_wrapper(func):
    def wrapper(*args, **kwargs):
        # Convert TensorFlow tensors to numpy arrays
        args = [arg.numpy() if isinstance(arg, tf.Tensor) else arg for arg in args]
        kwargs = {k: v.numpy() if isinstance(v, tf.Tensor) else v for k, v in kwargs.items()}
        
        # Call the original python function
        result = func(*args, **kwargs)
        
        # Convert the result back to a TensorFlow tensor
        return tf.convert_to_tensor(result)
    
    return wrapper

# Example usage
@py_function_wrapper
def add_one(x):
    return x + 1

# Test the wrapped function
x = tf.constant([1, 2, 3])
y = add_one(x)
print(y.numpy())  # Output: [2 3 4]
