
import tensorflow as tf

# Define a simple function to add two numbers
def add(a, b):
    return a + b

# Convert the function to a TensorFlow graph
graph = tf.function(add)

# Print the graph definition
print(graph.definition)
