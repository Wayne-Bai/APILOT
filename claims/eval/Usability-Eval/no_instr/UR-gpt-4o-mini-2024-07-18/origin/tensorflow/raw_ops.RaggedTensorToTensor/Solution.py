import tensorflow as tf

def convert_ragged_to_dense(ragged_tensor):
    # Convert a RaggedTensor to a dense tensor
    dense_tensor = ragged_tensor.to_tensor(default_value=0)
    return dense_tensor

# Example usage
ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
dense_tensor = convert_ragged_to_dense(ragged_tensor)

print(dense_tensor)
