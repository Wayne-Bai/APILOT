import tensorflow as tf

# Create a multi-dimensional array with dimensions 2x3x4
arr = tf.reshape(tf.range(0,24), (2,3,4))

# Print the multi-dimensional array
print(arr)
