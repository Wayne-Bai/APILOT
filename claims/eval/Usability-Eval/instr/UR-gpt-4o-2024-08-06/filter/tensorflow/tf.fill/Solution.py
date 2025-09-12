import tensorflow as tf

# Define the shape of the tensor
shape = (3, 3)

# Define the scalar value to fill the tensor
scalar_value = 7

# Create a tensor filled with the scalar value
tensor = tf.fill(shape, scalar_value)

# Print the tensor
print(tensor)
