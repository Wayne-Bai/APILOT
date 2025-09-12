import tensorflow as tf

# Define a function to be compiled into a TensorFlow graph
def func_to_compile(x, y):
    return tf.add(x, y)

# Use the tf.function decorator to compile the function into a graph
@tf.function
def compiled_func(x, y):
    return func_to_compile(x, y)

# Test the function
result = compiled_func(tf.constant(1), tf.constant(2))
print(result)
