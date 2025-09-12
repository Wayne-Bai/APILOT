import tensorflow as tf

def eager_function(input_tensor):
    # Your function logic here
    return input_tensor * 2

eager_op = tf.py_function(eager_function, [input_tensor], tf.int32)
