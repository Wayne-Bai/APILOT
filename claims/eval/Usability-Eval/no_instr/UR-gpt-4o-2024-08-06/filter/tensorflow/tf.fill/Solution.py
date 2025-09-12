import tensorflow as tf

# Define the shape of the tensor and the scalar value to fill it with
shape = (3, 3)  # Example shape
scalar_value = 5.0  # Example scalar value

# Create a tensor filled with the scalar value
filled_tensor = tf.constant(scalar_value, shape=shape)

# Print the resulting tensor
print(filled_tensor)
