import tensorflow as tf

def eager_python_func(x):
    # Your Python logic here
    return x * 2

@tf.function
def tf_eager_python_func(x):
    return tf.py_function(eager_python_func, [x], tf.int32)
