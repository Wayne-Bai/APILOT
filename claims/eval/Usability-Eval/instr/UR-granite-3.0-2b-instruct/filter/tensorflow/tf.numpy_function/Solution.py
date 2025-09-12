import tensorflow as tf

# Define your Python function
def python_function(x):
    return tf.square(x)

# Wrap the Python function as a TensorFlow op
@tf.function
def tensorflow_op(x):
    return python_function(x)

# Create a TensorFlow tensor
x = tf.constant(3.0)

# Use the TensorFlow op
result = tensorflow_op(x)

# Print the result
print(result)
