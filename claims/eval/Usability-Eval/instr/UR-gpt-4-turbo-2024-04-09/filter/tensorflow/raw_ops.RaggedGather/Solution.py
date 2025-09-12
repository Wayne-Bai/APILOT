import tensorflow as tf

def gather_ragged_slices(params, indices):
    # Create a constant tensor for the indices
    indices_tensor = tf.constant(indices)

    # Gather the ragged slices based on the indices
    gathered_slices = tf.gather(params, indices_tensor, axis=0)
    
    return gathered_slices

# Example usage
params = tf.ragged.constant([[1, 2, 3], [4], [5, 6]])
indices = [2, 0]

result = gather_ragged_slices(params, indices)
print(result)
