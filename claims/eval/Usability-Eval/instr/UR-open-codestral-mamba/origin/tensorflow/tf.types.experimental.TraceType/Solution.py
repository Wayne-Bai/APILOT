import tensorflow as tf

# We define a dummy function to use for specifying the Python API object types.
@tf.function
def f(x, y):
    return x**2 + y
