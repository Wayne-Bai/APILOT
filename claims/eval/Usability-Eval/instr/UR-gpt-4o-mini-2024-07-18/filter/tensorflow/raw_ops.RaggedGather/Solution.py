import tensorflow as tf

def gather_ragged_slices(params, indices):
    # Creating a RaggedTensor from params
    ragged_tensor = tf.ragged.constant(params)

    # Using tf.gather to gather slices based on indices
    gathered_tensor = tf.gather(ragged_tensor, indices)

    return gathered_tensor

# Example usage
params = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
indices = [1, 0]
result = gather_ragged_slices(params, indices)
print(result.to_list())
