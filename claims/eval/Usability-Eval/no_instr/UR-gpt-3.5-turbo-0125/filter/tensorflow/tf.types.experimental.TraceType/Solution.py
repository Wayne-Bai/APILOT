
import tensorflow as tf

@tf.function
def my_function(x, y):
    return x + y

# Tracing the function with example inputs
x = tf.constant(1, dtype=tf.int32)
y = tf.constant(2, dtype=tf.int32)
z = my_function(x, y)

# Checking the trace for object types
print(my_function.python_function.function_spec.input_signature)
