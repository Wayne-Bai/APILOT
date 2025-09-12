
import tensorflow as tf
from tensorflow.python.ops import script_ops

def my_function(x):
    # Your Python code here
    return x + 1

my_op = script_ops.wrap_py_func(my_function, [tf.int32], tf.int32)
