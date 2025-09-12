
import tensorflow as tf

# Create a tensor with some data
data = tf.constant([[1., 2., 3.], [4., 5., 6.]])

# Create a resource pointing to the tensor
resource = tf.raw_ops.Gather(data, [0, 1], validate_indices=False)

# Gather slices from the resource
slices = tf.raw_ops.Gather(resource, [0, 1], validate_indices=False)
