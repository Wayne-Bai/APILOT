import tensorflow as tf

# Define a simple Python function you want to use as a TensorFlow op
def simple_func(x, y):
    return x + y

# Wrap the Python function to use it as a TensorFlow operation
@tf.function
def tensorflow_op(x, y):
    return tf.numpy_function(simple_func, [x, y], tf.float32)

# Example inputs
x = tf.constant(1.0)
y = tf.constant(2.0)

# Use the wrapped operation
result = tensorflow_op(x, y)

# Run the operation and print the result
print(result)  # Should print: tf.Tensor(3.0, shape=(), dtype=float32)
