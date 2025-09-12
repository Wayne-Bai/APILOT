import tensorflow as tf

# Function to gather ragged slices from params along axis 0 according to indices
def gather_ragged_slices(params, indices):
    # Create a ragged tensor from the params
    ragged_tensor = tf.ragged.constant(params)
    
    # Use tf.gather to gather the specified slices based on indices
    gathered_slices = tf.gather(ragged_tensor, indices)

    return gathered_slices

# Example usage
params = [[1, 2], [3, 4], [5, 6]]
indices = [0, 2]

result = gather_ragged_slices(params, indices)
print(result)
