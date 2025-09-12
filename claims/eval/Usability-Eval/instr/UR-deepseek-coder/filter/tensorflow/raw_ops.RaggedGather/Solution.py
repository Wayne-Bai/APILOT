import tensorflow as tf

def gather_ragged_slices(params, indices):
    # Convert indices to a Tensor if it's not already
    indices = tf.convert_to_tensor(indices, dtype=tf.int32)
    
    # Gather slices from params axis 0 according to indices
    gathered_slices = tf.gather(params, indices)
    
    return gathered_slices

# Example usage:
params = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
indices = [0, 2]

result = gather_ragged_slices(params, indices)
print(result)
