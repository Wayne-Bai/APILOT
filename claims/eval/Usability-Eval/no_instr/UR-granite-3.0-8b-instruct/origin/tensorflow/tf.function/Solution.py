import tensorflow as tf

# Define a simple function
def simple_function(x):
    return x * 2

# Compile the function into a TensorFlow graph
simple_function_tf = tf.function(simple_function)

# Now you can use the compiled function
result = simple_function_tf(5)
print(result)  # Output: 10
