
import tensorflow as tf

# Define the python function
def my_function(x):
    return x**2 + 1

# Create a TensorFlow op from the python function
my_op = tf.py_function(my_function, [tf.constant([3.0])], tf.float32)

# Use the op in a TensorFlow graph
result = my_op()
print(result)  # prints 10.0
