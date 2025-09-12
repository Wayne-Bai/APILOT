import tensorflow as tf

# Create a tensor filled with a scalar value
scalar_value = 5
tensor_shape = [3, 3]  # Example shape
tensor_filled = tf.fill(tensor_shape, scalar_value)

print(tensor_filled)
