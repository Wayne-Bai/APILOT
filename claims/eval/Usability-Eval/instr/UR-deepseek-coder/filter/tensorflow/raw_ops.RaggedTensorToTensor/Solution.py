import tensorflow as tf

def dense_from_ragged(ragged_tensor, target_shape=None):
    # Convert the ragged tensor to a dense tensor
    dense_tensor = ragged_tensor.to_tensor()
    
    # If a target shape is provided, reshape the dense tensor
    if target_shape is not None:
        dense_tensor = tf.reshape(dense_tensor, target_shape)
    
    return dense_tensor

# Example usage:
# ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
# dense_tensor = dense_from_ragged(ragged_tensor, target_shape=[3, 3])
# print(dense_tensor)
