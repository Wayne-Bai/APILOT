import tensorflow as tf

# Define the shape of the DTensor
shape = (2, 3, 4)

# Create a DTensor with the defined shape
dtensor = tf.dynamic_random_shape(shape)

# Print the shape of the DTensor
print("Shape of the DTensor:", dtensor.shape)
