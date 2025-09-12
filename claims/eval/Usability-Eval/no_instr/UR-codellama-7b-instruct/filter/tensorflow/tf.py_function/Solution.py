
import tensorflow as tf

def my_python_function(x, y):
    return x + y

@tf.custom_gradient
def my_tensorflow_op(x, y):
    result = my_python_function(x, y)
    def grad(dy):
        return tf.convert_to_tensor([1, 2])
    return result, grad
