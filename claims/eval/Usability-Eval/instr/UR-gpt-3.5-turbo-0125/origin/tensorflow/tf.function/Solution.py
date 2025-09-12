
import tensorflow as tf

@tf.function
def my_function(x):
    return x * x + 2

graph = my_function.get_concrete_function(tf.TensorSpec(None, tf.float32))

print(graph)
