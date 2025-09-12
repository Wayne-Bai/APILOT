import tensorflow as tf

def tf_function(func):
    @tf.function
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
