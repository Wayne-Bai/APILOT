import tensorflow as tf

# Define a Python function
def my_python_func(x):
    """A simple Python function that squares its input."""
    return x ** 2

# Use tf.py_function to wrap the Python function
def my_tf_func(x):
    """A TensorFlow function that wraps `my_python_func`."""
    return tf.py_function(func=my_python_func, inp=[x], Tout=[tf.float64])

# Create a TensorFlow graph
x = tf.constant(2.0)
y = my_tf_func(x)

# Run the TensorFlow graph
with tf.Session() as sess:
    result = sess.run(y)
    print(result)
