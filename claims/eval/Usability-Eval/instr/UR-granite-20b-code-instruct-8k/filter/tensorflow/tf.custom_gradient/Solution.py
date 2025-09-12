import tensorflow as tf

def custom_gradient_decorator(func):
    """
    Decorator to define a function with a custom gradient.
    """
    def wrapper(*args, **kwargs):
        y = func(*args, **kwargs)
        grad_fn = tf.custom_gradient(func)(*args, **kwargs)
        return y, grad_fn
    return wrapper
