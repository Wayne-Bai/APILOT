import tensorflow as tf
from tensorflow.python.framework import ops

def my_cool_func(x, y):
    return x + y

# Wrap the Python function
wrapped_func = ops.Gofer.add_method(ops.Tensor, 'my_cool_func', my_cool_func)

# Now you can use the wrapped function like a tensorflow op
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])
result = a.my_cool_func(b)
