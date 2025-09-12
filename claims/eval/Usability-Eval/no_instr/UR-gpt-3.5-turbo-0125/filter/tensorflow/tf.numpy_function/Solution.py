
import tensorflow as tf

def my_python_function(x):
    return x + 1

@tf.function
def my_tf_op(x):
    return tf.py_function(my_python_function, [x], tf.float32)

# Example usage
input_data = tf.constant(1.0)
output_data = my_tf_op(input_data)

print(output_data)
