# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create a TensorFlow session
session = tf.Session()

# Define a custom initializer with a constant value
class CustomInitializer(tfInitializer):
    def __init__(self, value=0):
        self.value = value

    def __call__(self, shape, dtype=None):
        return tf.constant(self.value, shape=shape, dtype=dtype)

# Create a variable with the custom initializer
var = tf.get_variable('var', shape=[2,3], initializer=CustomInitializer(5))

# Initialize the variable
session.run(tf.global_variables_initializer())

# Print the variable's value
print(session.run(var))  # Output: [[5 5 5], [5 5 5]]

# Define a three-dimensional constant tensor
my_constant = tf.constant(25, shape=[1, 3, 4])

# Print the constant tensor's values
print(session.run(my_constant))  # Output: [[[25 25 25 25]]]
