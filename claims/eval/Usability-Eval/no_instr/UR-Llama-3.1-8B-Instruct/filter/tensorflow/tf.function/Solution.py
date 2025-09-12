import tensorflow as tf

# Define a simple function that we want to compile into a TensorFlow graph
def my_function(x):
    return tf.sin(x) + tf.cos(2*x)

# Compile the function into a callable TensorFlow graph
executor = tf.function(my_function).get_concrete_function(tf.TensorShape([1]))

# Now we can use the function like any other TensorFlow function
print("First Result:")
print(executor([1.0]))  # Output: tf.Tensor(-0.84861956, shape=(), dtype=float32)

# We can also define inputs and outputs for the function
inputs = tf.TensorShape([None])  # input to function
outputs = tf.TensorSpec([1], tf.float32)  # output from function

# Compile the function for multiple inputs
function = tf.function(my_function)
compiled_function = function.get_concrete_function(inputs, outputs)

# Now we can use the function with multiple inputs
print("\nMultiple Inputs:")
print(compiled_function([1.0, 2.0, 3.0]))
