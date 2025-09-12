import tensorflow as tf

def python_function(func, inp, Tout, name=None):
    def wrapped_func(*inputs):
        output = func(*inputs)
        return tf.convert_to_tensor(output)

    return tf.py_function(wrapped_func, inp, Tout, name=name)

# example usage
def my_python_func(x):
    return x*2

x = tf.constant([1,2,3,4])
tf_output = python_function(my_python_func, [x], tf.int32)
