import tensorflow as tf

def gather_ragged_slices(params, indices):
    # Ensure params is a RaggedTensor
    if not isinstance(params, tf.RaggedTensor):
        params = tf.ragged.constant(params)

    # Gather ragged slices using tf.gather
    gathered = tf.gather(params, indices)
    return gathered

# Example usage
params = tf.ragged.constant([[1, 2, 3], [4], [5, 6]])
indices = [2, 0]
result = gather_ragged_slices(params, indices)
print(result)  # Output: <tf.RaggedTensor [[5, 6], [1, 2, 3]]>
