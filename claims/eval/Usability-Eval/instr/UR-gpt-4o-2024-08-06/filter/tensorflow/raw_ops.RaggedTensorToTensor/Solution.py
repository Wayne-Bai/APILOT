import tensorflow as tf

# Function to convert a ragged tensor to a dense tensor with specified shape
def ragged_to_dense(ragged_tensor, default_value=0, dense_shape=None):
    # Convert the ragged tensor to a dense tensor
    # Using tf.ragged.fill_empty_rows and then converting to dense
    dense_tensor = ragged_tensor.to_tensor(default_value=default_value)
    
    # If a specific dense shape is required, reshape the dense tensor
    if dense_shape is not None:
        dense_tensor = tf.reshape(dense_tensor, shape=dense_shape)

    return dense_tensor

# Example usage
ragged_tensor = tf.ragged.constant([[1, 2], [], [3, 4, 5]])
default_value = 0
dense_shape = [3, 4]  # This will reshape the dense tensor to a 3x4 shape

dense_tensor = ragged_to_dense(ragged_tensor, default_value, dense_shape)
print(dense_tensor.numpy())
