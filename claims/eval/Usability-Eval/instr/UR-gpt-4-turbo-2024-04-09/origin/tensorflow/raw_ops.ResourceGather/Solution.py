import tensorflow as tf

# Assuming 'resource' is a TensorFlow variable and 'indices' is a list or tensor of indices
# For instance, let's create a sample resource variable and indices
resource = tf.Variable([[1, 2], [3, 4], [5, 6], [7, 8]])
indices = [0, 2]

# Using tf.raw_ops to gather slices
gathered_slices = tf.raw_ops.ResourceGather(resource=resource.handle, indices=indices)

print(gathered_slices)
