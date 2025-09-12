import tensorflow as tf

# Create a scalar value
scalar_value = 10

# Create a tensor filled with the scalar value
tensor = tf.fill([1, 1], scalar_value)

# Print the tensor
print(tensor)
