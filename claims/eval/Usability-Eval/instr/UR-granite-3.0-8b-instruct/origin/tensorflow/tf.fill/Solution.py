import tensorflow as tf

# Create a tensor filled with a scalar value
scalar_value = 5
tensor = tf.fill((3, 3), scalar_value)

print(tensor)
