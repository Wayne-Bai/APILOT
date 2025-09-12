
import tensorflow as tf

# Define a Python function that takes two inputs and returns their sum
def add(a, b):
  return a + b

# Compile the function using `tf.function`
add_graph = tf.function(add)

# Run the graph with some input data
inputs = [1.0, 2.0]
output = add_graph(inputs)
print(output)  # prints 3.0
