import tensorflow as tf

# Create a 1D tensor of flat indices
indices = tf.constant([0, 2, 4, 6], dtype=tf.int32)

# Create a 2D tensor with the same number of elements as the indices tensor
# The shape of the tensor will be (num_elements, 2)
coordinates = tf.raw_ops.ConvertIndicesToCoordinates(indices=indices, num_elements=tf.size(indices))

# Print the coordinates tensor
print(coordinates)
