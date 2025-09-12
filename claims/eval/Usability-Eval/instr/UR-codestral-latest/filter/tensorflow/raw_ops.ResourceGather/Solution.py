import tensorflow as tf

# Example usage of tf.raw_ops.ResourceGather
resource = tf.Variable([1, 2, 3, 4, 5])
indices = tf.constant([0, 2, 4])

# Gather slices from the variable according to indices
result = tf.raw_ops.ResourceGather(resource=resource.handle, indices=indices)

print(result)
