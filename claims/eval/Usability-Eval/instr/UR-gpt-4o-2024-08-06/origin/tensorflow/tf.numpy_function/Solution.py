import tensorflow as tf

# Define a Python function
def my_python_function(x):
    return x ** 2 + 2 * x + 1

# Use tf.py_function to wrap the Python function
def my_tf_function(x):
    # Specify output type
    y = tf.py_function(func=my_python_function, inp=[x], Tout=tf.float32)
    return y

# Define a TensorFlow input tensor
x = tf.constant(3.0, dtype=tf.float32)

# Use the TensorFlow function
y = my_tf_function(x)

# Evaluate the result
print("Result:", y.numpy())
