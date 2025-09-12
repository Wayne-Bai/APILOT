import tensorflow as tf

def gradient_aware_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        grad = tf.gradients(result, var_list)[0]  # Assuming `var_list` is defined elsewhere in the decorator context
        return result, grad

    return wrapper

# Usage example
@gradient_aware_decorator
def my_function(x):
    return x ** 2

result, grad = my_function(2.0)
print(result, grad)
