import tensorflow as tf

def optimize_tracing(func):
    def wrapper(*args, **kwargs):
        # Convert arguments annotated with tf.Tensor to Tensor
        args = [tf.convert_to_tensor(arg) if isinstance(arg, tf.Tensor) else arg for arg in args]
        kwargs = {key: tf.convert_to_tensor(value) if isinstance(value, tf.Tensor) else value for key, value in kwargs.items()}
        
        # Call the original function with the converted arguments
        return func(*args, **kwargs)
    
    return wrapper

# Example usage
@optimize_tracing
def example_function(a: tf.Tensor, b: tf.Tensor) -> tf.Tensor:
    return a + b

# Test the function
a = tf.constant([1.0, 2.0])
b = tf.constant([3.0, 4.0])
result = example_function(a, b)
print(result)  # Output: tf.Tensor([4. 6.], shape=(2,), dtype=float32)
