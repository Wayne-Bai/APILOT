import tensorflow as tf

# Define a function
@tf.function
def my_function(x):
    return tf.square(x)

# Create a tensor
x = tf.constant(5.0)

# Call the function with the tensor
result = my_function(x)

# Print the result
print(result)
