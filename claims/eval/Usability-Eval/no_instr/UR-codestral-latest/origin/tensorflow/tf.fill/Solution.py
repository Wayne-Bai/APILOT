import tensorflow as tf

# Define the scalar value
scalar_value = 5

# Create a tensor filled with the scalar value
tensor = tf.fill((3, 3), scalar_value)

print(tensor)
