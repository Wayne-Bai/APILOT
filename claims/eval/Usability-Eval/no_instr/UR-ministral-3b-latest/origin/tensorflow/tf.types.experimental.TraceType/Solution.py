import tensorflow as tf

def my_function(x):
    # Dummy function to demonstrate tf.function tracing
    y = x * 2
    return y

# Decorate the function with tf.function for tracing
@tf.function
def wrapped_function(x):
    return my_function(x)

# Now, wrapped_function is traced and optimized for execution.
