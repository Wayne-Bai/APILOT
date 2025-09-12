import tensorflow as tf

# Define a simple Python function
def my_python_function(x):
    return x ** 2 + 2 * x + 1

# Wrap the Python function in a TensorFlow op
@tf.function
def wrapped_function(x):
    # Use tf.py_function to wrap the Python function
    return tf.py_function(func=my_python_function, inp=[x], Tout=tf.float32)

# Demonstrate the wrapped function with TensorFlow tensors
input_tensor = tf.constant(3.0, dtype=tf.float32)
result = wrapped_function(input_tensor)

# Print the result
tf.print(result)
