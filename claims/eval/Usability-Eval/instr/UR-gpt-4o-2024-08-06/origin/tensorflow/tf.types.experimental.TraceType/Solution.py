import tensorflow as tf

# Define a simple function to be used with tf.function
@tf.function
def simple_add(a, b):
    return a + b

# Example usage of the function with tensor inputs
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])

# Call the function
result = simple_add(a, b)

print("Result of addition:", result)

# For a different object tracing (demonstrating different types passed to tf.function)
@tf.function
def multiply_and_add(a, b, c):
    return a * b + c

# Example usage of the function with tensor inputs
c = tf.constant([7, 8, 9])

# Call the function
result = multiply_and_add(a, b, c)

print("Result of multiply and add:", result)
