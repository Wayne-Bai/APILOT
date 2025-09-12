import tensorflow as tf

def create_dense_from_ragged(ragged_tensor, new_shape=None):
    # Convert the RaggedTensor to a dense tensor
    dense_tensor = ragged_tensor.to_tensor()

    # If a new shape is provided, reshape the dense tensor
    if new_shape:
        dense_tensor = tf.reshape(dense_tensor, new_shape)

    return dense_tensor

# Example usage
ragged_tensor = tf.ragged.constant([[1, 2], [3, 4, 5]])
dense_tensor = create_dense_from_ragged(ragged_tensor, new_shape=[2, 3])
print(dense_tensor)
