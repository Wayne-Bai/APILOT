
import tensorflow as tf

# Create a Tensorflow constant with the flat indices
flat_indices = tf.constant([0, 1, 2, 3, 4])

# Define the shape of the tensor
tensor_shape = [2, 3]

# Use tf.raw_ops method to convert flat indices to coordinate arrays
coordinates = tf.raw_ops.UnravelIndex(indices=flat_indices, dims=tensor_shape)

# Start a Tensorflow session to execute the operation
with tf.Session() as sess:
    result = sess.run(coordinates)
    print(result)
