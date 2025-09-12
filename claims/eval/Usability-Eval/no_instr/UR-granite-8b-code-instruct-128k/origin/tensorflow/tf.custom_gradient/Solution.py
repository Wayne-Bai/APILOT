
import tensorflow as tf

def custom_gradient(func):
    def wrapper(*args, **kwargs):
        with tf.GradientTape() as tape:
            tape.watch(args)
            tape.watch(kwargs)
            result = func(*args, **kwargs)
        grad = tape.gradient(result, args + tuple(kwargs.values()))
        return result, grad
    return wrapper
