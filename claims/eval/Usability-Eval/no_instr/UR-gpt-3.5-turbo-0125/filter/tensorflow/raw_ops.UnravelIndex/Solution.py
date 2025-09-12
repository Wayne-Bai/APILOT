
import tensorflow as tf

# Create flat indices tensor
flat_indices = tf.constant([0, 1, 2, 3, 4, 5])

# Define the shape of the tensor that the flat indices correspond to
tensor_shape = tf.constant([2, 3])

# Use tf.raw_ops.UnravelIndex to convert flat indices to tensor coordinates
output_tensor_coordinates = tf.raw_ops.UnravelIndex(indices=flat_indices, dims=tensor_shape)

with tf.Session() as sess:
    result = sess.run(output_tensor_coordinates)
    print(result)
