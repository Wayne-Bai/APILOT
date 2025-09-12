import tensorflow as tf

# Function to convert a ragged tensor to a dense tensor
def ragged_to_dense(ragged_tensor):
    # Convert ragged tensor to dense tensor
    dense_tensor = ragged_tensor.to_dense()
    return dense_tensor

# Example usage
ragged_example = tf.ragged.constant([
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
])

dense_output = ragged_to_dense(ragged_example)
print(dense_output)
