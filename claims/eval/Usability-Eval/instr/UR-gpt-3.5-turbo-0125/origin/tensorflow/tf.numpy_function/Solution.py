
import tensorflow as tf

@tf.function
def my_tf_function(x):
    return tf.py_function(my_python_function, inp=[x], Tout=tf.float32)

def my_python_function(x):
    # Add your python function logic here
    result = x + 1
    return result

# Usage example
input_value = tf.constant(5, dtype=tf.float32)
output_value = my_tf_function(input_value)
print(output_value)
