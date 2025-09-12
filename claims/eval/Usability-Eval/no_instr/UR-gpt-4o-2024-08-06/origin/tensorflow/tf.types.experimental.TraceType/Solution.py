import tensorflow as tf

# Define a simple function using tf.function
@tf.function
def my_function(x):
    return x * x

# Create a TensorSpec which represents the type of inputs to the function for tracing
x_type = tf.TensorSpec(shape=None, dtype=tf.float32)

# Trace the function using the specified input type
concrete_function = my_function.get_concrete_function(x_type)

# Print the traced concrete function details
print(concrete_function)
