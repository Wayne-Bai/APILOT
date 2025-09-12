
import tensorflow as tf

# Create a function using tf.raw_ops to encode a RaggedTensor into a variant Tensor
def encode_ragged_tensor(ragged_tensor):
    encoded_tensor = tf.raw_ops.EncodeRaggedTensor(values=ragged_tensor.values, row_splits=ragged_tensor.row_splits)
    return encoded_tensor

# Example usage
values = tf.constant([1, 2, 3, 4, 5, 6])
row_splits = tf.constant([0, 2, 3, 6])
ragged_tensor = tf.RaggedTensor.from_row_splits(values, row_splits)

encoded_tensor = encode_ragged_tensor(ragged_tensor)
print(encoded_tensor)
