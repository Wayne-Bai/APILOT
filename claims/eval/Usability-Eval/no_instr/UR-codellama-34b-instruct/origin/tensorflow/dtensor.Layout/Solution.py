
import tensorflow as tf

# Define the shape and type of the DTensor
shape = (2, 3)
dtype = tf.float64

# Create a DTensor with the given shape and type
dtensor = tf.zeros(shape, dtype=dtype)

# Print the layout information of the DTensor
print("DTensor layout:")
print(dtensor.get_layout())
