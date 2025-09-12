import tensorflow as tf

# Example usage of ragged slices from params axis 0 according to indices
def gather_ragged_slices(params, indices):
    # Transform params into a ragged tensor
    ragged_tensor = tf.RaggedTensor.from_row_splits(params, tf.constant([0, 3, 5, 6]))

    # Gather ragged slices according to indices
    gathered = tf.gather(ragged_tensor, indices)

    return gathered

# Example parameters and indices
params = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
indices = [0, 2]

# Call the function and print the result
result = gather_ragged_slices(params, indices)
print(result)
