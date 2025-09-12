import tensorflow as tf

# Create a tensor filled with a scalar value
scalar_value = 42
tensor = tf.fill([2, 3], scalar_value)

print(tensor)
