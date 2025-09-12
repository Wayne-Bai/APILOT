import tensorflow as tf

def dense_from_ragged(ragged_tensor, desired_shape=None):
    # Convert the ragged tensor to a dense tensor
    dense_tensor = ragged_tensor.to_tensor(default_value=0)
    
    # If a desired shape is provided, reshape the dense tensor
    if desired_shape is not None:
        dense_tensor = tf.reshape(dense_tensor, desired_shape)
    
    return dense_tensor

# Example usage:
# Create a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2], [3, 4, 5], [6]])

# Convert to dense tensor with a desired shape
desired_shape = [3, 3]
dense_tensor = dense_from_ragged(ragged_tensor, desired_shape)

print(dense_tensor)
