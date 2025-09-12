import tensorflow as tf

def add_two_numbers(x, y):
    return x + y

# Wraps a python function into a TensorFlow op that executes it eagerly
# Create TensorFlow ops that return arithmetic operations
add_two_numbers_tf = tf.function(add_two_numbers)

# Define two constant tensors
x = tf.constant(5)
y = tf.constant(7)

# Call the function and print the results
print(add_two_numbers_tf(x, y).numpy())
