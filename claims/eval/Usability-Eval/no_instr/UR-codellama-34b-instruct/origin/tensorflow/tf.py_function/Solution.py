
import tensorflow as tf

# Define the function to be wrapped in an op
def my_function(x):
    # Do something with x
    return x + 1

# Create a TensorFlow op that executes the function eagerly
@tf.function(experimental_compile=True)
def my_op(inputs, name=None):
    # Eagerly execute the function on the input tensors
    result = my_function(inputs)
    # Return the result as a TensorFlow tensor
    return tf.convert_to_tensor(result, name=name)
