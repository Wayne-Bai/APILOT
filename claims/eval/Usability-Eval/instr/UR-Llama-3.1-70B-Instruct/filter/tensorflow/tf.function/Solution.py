# Import necessary libraries
import tensorflow as tf

# Define a simple function
@tf.function
def my_function(x, y):
    """
    Simple function that adds two numbers.
    
    Args:
        x (int or float): The first number.
        y (int or float): The second number.
    
    Returns:
        int or float: The sum of x and y.
    """
    return tf.add(x, y)

# Convert the function to a callable TensorFlow graph
my_graph = tf.function(my_function)

# Test the compiled function
print(my_graph(1, 2))  # Outputs: 3

# You can also inspect the compiled function
print(tf.autograph.to_code(my_function))  # Prints the compiled code
