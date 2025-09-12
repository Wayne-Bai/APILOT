import tensorflow as tf

# Define a simple function
@tf.function
def math_operation(x, y):
    return x * y + 2

# Create TensorFlow constants
x = tf.constant(5.0)
y = tf.constant(3.0)

# Execute the compiled function
result = math_operation(x, y)

# Print the result
print("Result of the operation:", result.numpy())
