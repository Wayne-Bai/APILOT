
import tensorflow as tf

# Define your function here
def my_function(x):
    return x * 2

# Convert the function to a TensorFlow graph
graph = tf.function(my_function)

# Test the graph
print(graph(5))  # Output: 10
