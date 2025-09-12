import tensorflow as tf

def convert_to_tensor(func):
    def wrapper(*args, **kwargs):
        # Convert arguments to tensors based on type annotations
        annotations = func.__annotations__
        for i, arg in enumerate(args):
            if i < len(func.__code__.co_varnames):
                var_name = func.__code__.co_varnames[i]
                if var_name in annotations and annotations[var_name] == tf.Tensor:
                    args = list(args)
                    args[i] = tf.convert_to_tensor(arg)
        
        for key, value in kwargs.items():
            if key in annotations and annotations[key] == tf.Tensor:
                kwargs[key] = tf.convert_to_tensor(value)
        
        # Call the function with the converted arguments
        return func(*args, **kwargs)
    
    return wrapper

# Example usage:

@convert_to_tensor
def add(x: tf.Tensor, y: int) -> tf.Tensor:
    return x + y

# Test the function
print(add(5, 3))  # Output: tf.Tensor(8, shape=(), dtype=int32)
