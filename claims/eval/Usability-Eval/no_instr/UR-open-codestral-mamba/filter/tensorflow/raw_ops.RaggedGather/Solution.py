
import tensorflow as tf

def gather_ragged_slices(params, indices):
    # Reshape indices to 2D
    indices = tf.expand_dims(tf.expand_dims(indices, 0), 1)

    # Create a ragged tensor from params
    r = tf.RaggedTensor.from_tensor(params)

    # Gather slices based on indices
    gathered = tf.raw_ops.GatherNd(params=r.to_tensor(), indices=indices)

    return gathered

# Test the function
params = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
indices = tf.constant([0, 2])
print(gather_ragged_slices(params, indices))

