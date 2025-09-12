import tensorflow as tf

def gather_ragged_slices(params, indices):
    # Convert params to a RaggedTensor if it's not already
    if not isinstance(params, tf.RaggedTensor):
        params = tf.RaggedTensor.from_tensor(params)
    
    # Gather ragged slices from params axis 0 according to indices
    gathered_slices = tf.gather(params, indices)
    
    return gathered_slices

# Example usage:
params = tf.ragged.constant([[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]])
indices = [1, 3]
result = gather_ragged_slices(params, indices)
print(result)
