
import tensorflow as tf

# Define the shape of the multidimensional array
shape = (3, 4)

# Initialize the multidimensional array with random values
array = tf.random_normal(shape=shape)

# Print the shape and content of the array
print("Shape:", shape)
print("Content:", array)
