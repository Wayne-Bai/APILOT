import tensorflow as tf

def gather_ragged_slices(params, indices):
    # Flatten the indices to handle ragged tensors
    flat_indices = tf.ragged.boolean_mask(indices, tf.ones_like(indices, dtype=tf.bool))
    
    # Gather slices from params using the flattened indices
    gathered_slices = tf.gather(params, flat_indices)
    
    return gathered_slices

# Example usage:
params = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
indices = tf.ragged.constant([[0, 1], [0], [1, 2]])

result = gather_ragged_slices(params, indices)
print(result)
