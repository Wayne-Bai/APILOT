# Import necessary libraries
import tensorflow as tf

# Define a simple function
@tf.function
def simple_function(x, y):
    """
    A simple function that adds two numbers and multiplies by a constant.
    
    Args:
    x (tf.Tensor): The first number.
    y (tf.Tensor): The second number.
    
    Returns:
    tf.Tensor: The result of the operation.
    """
    constant = tf.constant(2.0)
    result = tf.add(x, y)
    result = tf.multiply(result, constant)
    return result

# Create input tensors
x = tf.constant(1.0)
y = tf.constant(3.0)

# Call the compiled function
result = simple_function(x, y)

# Print the result
print(result)
