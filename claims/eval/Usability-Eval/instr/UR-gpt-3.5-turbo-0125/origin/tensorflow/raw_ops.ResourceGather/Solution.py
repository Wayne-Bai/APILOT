
import tensorflow as tf

@tf.function
def gather_slices_from_variable(resource, indices):
    return tf.raw_ops.ResourceGather(ref=resource, indices=indices)

# Example usage
resource = tf.Variable([10, 20, 30, 40])
indices = tf.constant([1, 3])
result = gather_slices_from_variable(resource, indices)
print(result)
