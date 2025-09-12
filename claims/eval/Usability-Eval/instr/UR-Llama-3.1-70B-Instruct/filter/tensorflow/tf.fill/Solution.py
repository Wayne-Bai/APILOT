# Import the necessary library
import tensorflow as tf

# Define the scalar value to fill the tensor
scalar_value = 5

# Define the shape of the tensor
tensor_shape = [2, 3]

# Create a tensor filled with a scalar value
tensor = tf.fill(tensor_shape, scalar_value)

# Print the created tensor
print(tensor)
