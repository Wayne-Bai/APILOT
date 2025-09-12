
import tensorflow as tf

def my_func(x):
    return x**2 + 1

# Define the shape of the input and output tensors
shape = (10, 1)

# Create a tensor representing the input data
input_tensor = tf.ones(shape) * 2

# Wrap the Python function using tf.py_function
output_tensor = tf.py_function(my_func, [input_tensor], Tout=tf.float32)
