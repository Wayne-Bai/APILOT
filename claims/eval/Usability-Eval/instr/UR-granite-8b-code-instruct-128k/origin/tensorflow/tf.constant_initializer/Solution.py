import tensorflow as tf

# Define the constant value to initialize the tensors
constant_value = 0.5

# Create an initializer that generates tensors with the constant value
initializer = tf.constant_initializer(constant_value)

# Use the initializer to create a tensor
tensor = tf.Variable(initial_value=initializer, shape=[1, 2, 3])

# Print the tensor
print(tensor)
