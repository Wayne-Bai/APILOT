import tensorflow as tf

def py_function_wrapper(func):
    def wrapper(*args, **kwargs):
        def py_func(*args, **kwargs):
            return func(*args, **kwargs)
        
        # Convert the Python function to a TensorFlow op
        result = tf.py_func(py_func, args, Tout=tf.float32)
        return result
    
    return wrapper

# Example usage
@py_function_wrapper
def add_two_numbers(a, b):
    return a + b

# Create TensorFlow tensors
a = tf.constant(2.0)
b = tf.constant(3.0)

# Use the wrapped function
result = add_two_numbers(a, b)

# Run the TensorFlow session
with tf.Session() as sess:
    print(sess.run(result))
