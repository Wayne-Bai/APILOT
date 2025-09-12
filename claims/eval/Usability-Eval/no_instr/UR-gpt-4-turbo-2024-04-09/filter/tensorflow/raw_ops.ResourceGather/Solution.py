import tensorflow as tf

def gather_slices_from_resource(resource, indices):
    # Use the tf.raw_ops.ResourceGather method to gather slices from a resource variable
    return tf.raw_ops.ResourceGather(resource=resource, indices=indices, dtype=resource.dtype.base_dtype)

# Example usage
resource = tf.Variable([1, 2, 3, 4, 5])
indices = [1, 3]

result = gather_slices_from_resource(resource, indices)
print(result.numpy())
