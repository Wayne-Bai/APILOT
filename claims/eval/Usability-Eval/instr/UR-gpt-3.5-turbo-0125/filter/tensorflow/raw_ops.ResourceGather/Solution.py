
import tensorflow as tf

@tf.function
def gather_slices_from_resource(resource, indices):
    return tf.raw_ops.ResourceGather(resource=resource, indices=indices)

# Usage example
resource = tf.Variable([[1.0, 2.0], [3.0, 4.0]])
indices = tf.constant([0, 1])
result = gather_slices_from_resource(resource, indices)
print(result)
