
import tensorflow as tf

@tf.function
def eager_execution_python_function(my_function):
    return tf.py_function(my_function, inp=[], Tout=[])
