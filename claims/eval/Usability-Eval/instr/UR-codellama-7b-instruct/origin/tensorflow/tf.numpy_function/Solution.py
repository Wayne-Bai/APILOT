
import tensorflow as tf

def my_func(x):
    return x * x

@tf.function
def my_op(x):
    y = my_func(x)
    return y
