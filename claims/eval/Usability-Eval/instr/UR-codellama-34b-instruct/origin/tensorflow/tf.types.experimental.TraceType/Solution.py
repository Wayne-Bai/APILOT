
import tensorflow as tf

@tf.function
def my_function(x):
    return x * x

# To create a TensorFlow graph, we need to call the `get_concrete_function` method on the function object
my_graph = my_function.get_concrete_function()

print(my_graph)  # This will print the TensorFlow graph for the function
