import tensorflow as tf

def ragged_to_dense(ragged_tensor, default_value=0):
    # Convert the ragged tensor to a dense tensor.
    # Any missing values are filled with the default_value.
    dense_tensor = ragged_tensor.to_tensor(default_value)
    return dense_tensor

# Test the function with a sample ragged tensor
sample_ragged_tensor = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
print(ragged_to_dense(sample_ragged_tensor))
