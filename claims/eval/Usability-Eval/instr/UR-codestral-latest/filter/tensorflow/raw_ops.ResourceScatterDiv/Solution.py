import tensorflow as tf

def divide_sparse_updates(ref, indices, updates, name=None):
    with tf.name_scope(name, "divide_sparse_updates", [ref, indices, updates]):
        # Fetch the shape of the variable
        shape = ref.shape

        # Apply updates to the variable
        updated_ref = tf.tensor_scatter_nd_update(ref, indices, updates)

        # Divide the updated variable
        divided_ref = tf.math.divide(updated_ref, ref)

        return divided_ref

# Initialize the variable and the updates
ref = tf.Variable([1, 2, 3, 4, 5])
indices = tf.constant([[1], [3]])
updates = tf.constant([6, 8])

result = divide_sparse_updates(ref, indices, updates)

print(result.numpy())
