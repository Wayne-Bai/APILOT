import tensorflow as tf

# Define the function to apply to each element
def my_function(x):
    return tf.square(x)

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# Unstack the tensor on axis 0
unstacked_tensor = tf.unstack(tensor)

# Apply the function to each element
result = [my_function(x) for x in unstacked_tensor]

# Stack the results back together
result = tf.stack(result)

# Print the result
print(result)
