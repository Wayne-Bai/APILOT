import tensorflow as tf

# Define a python function that we want to wrap into a TensorFlow op
def my_python_function(x, y, z):
    return (x + y) * z

# Use tf.py_function to wrap the python function into a TensorFlow op
def wrap_function(x, y, z, name=None):
    return tf.py_function(
        func=my_python_function,  # The python function we want to wrap
        inp=[x, y, z],  # Input arguments
        Tout=tf.float32,  # Output type
        name=name  # Optional name for the operation
    )

# Create a TensorFlow session and execute the wrapped function
x = tf.constant([1, 2, 3])
y = tf.constant([4, 5, 6])
z = tf.constant([7, 8, 9])

output = wrap_function(x, y, z)

# Evaluate the output in TensorFlow's eager execution mode
output_eager = output.numpy()

# Print the output
print(output_eager)
