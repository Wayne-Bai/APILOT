
import tensorflow as tf

def my_function(x):
    return x ** 2 + 1

@tf.custom_gradient
def my_func_op(x):
    y = my_function(x)
    def grad(dy):
        dx = dy * 2 * x
        return (dx,)
    return y, grad
