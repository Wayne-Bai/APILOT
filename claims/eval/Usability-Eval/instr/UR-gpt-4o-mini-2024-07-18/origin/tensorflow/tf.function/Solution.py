import tensorflow as tf

# Define a simple TensorFlow function
@tf.function
def multiply(x, y):
    return x * y

# Create some example inputs
a = tf.constant(3)
b = tf.constant(4)

# Call the function
result = multiply(a, b)

print(result.numpy())  # Output: 12
