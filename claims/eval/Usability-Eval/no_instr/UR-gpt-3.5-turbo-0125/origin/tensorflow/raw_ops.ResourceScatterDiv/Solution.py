
import tensorflow as tf

@tf.function
def sparse_variable_update(resource, indices, values):
    return tf.raw_ops.ResourceSparseApplyGradientDescent(resource=resource, indices=indices, values=values)

# Example usage:
resource = tf.Variable(tf.ones((5, 5)))
indices = tf.constant([[1, 1], [2, 2]])
values = tf.constant([[0.5, 0.8], [-0.3, 0.1]])
update_op = sparse_variable_update(resource, indices, values)
print(resource)
