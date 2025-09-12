import tensorflow as tf

# Define a simple Python function to be wrapped as a TensorFlow op
def add_numbers(x, y):
    return x + y

# Use tf.py_function to wrap the Python function
@tf.function
def add_numbers_tf(x, y):
    return tf.py_function(func=add_numbers, inp=[x, y], Tout=tf.int32)

# Example usage with TensorFlow constants
x = tf.constant(3, dtype=tf.int32)
y = tf.constant(5, dtype=tf.int32)

# Call the wrapped TensorFlow op
result = add_numbers_tf(x, y)
print(result.numpy())  # This should output 8
