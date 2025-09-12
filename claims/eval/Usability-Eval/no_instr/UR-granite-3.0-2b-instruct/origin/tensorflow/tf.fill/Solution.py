import tensorflow as tf

# Create a scalar value
scalar_value = 10.0

# Create a tensor filled with the scalar value
tensor = tf.fill([10], scalar_value)

# Print the tensor
print(tensor)
