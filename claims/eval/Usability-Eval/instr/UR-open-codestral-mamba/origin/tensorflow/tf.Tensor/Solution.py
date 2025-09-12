import tensorflow as tf

# Generate a 3D array (Randomly)
mean = 0
stddev = 1
shape = (2, 2, 2)  # Define the shape of the array

array_3d = tf.random.normal(shape, mean, stddev)

print(array_3d)
