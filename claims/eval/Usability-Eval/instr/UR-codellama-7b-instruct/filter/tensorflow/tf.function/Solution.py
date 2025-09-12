
import tensorflow as tf

# Define a Python function that takes in two tensors and returns their product
def multiply(a, b):
    return a * b

# Convert the Python function to a callable TensorFlow graph
graph = tf.function(multiply)

# Use the callable graph to perform the computation
result = graph(tf.constant([1, 2]), tf.constant([3, 4]))
print(result)
