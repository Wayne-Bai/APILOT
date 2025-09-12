import tensorflow as tf

def encode_ragged_tensor_to_variant(input_values, input_row_splits, input_value_dtype, input_row_splits_dtype):
    """
    Encodes a RaggedTensor into a variant Tensor.

    Args:
    input_values: A `Tensor` of type `input_value_dtype`.
    input_row_splits: A `Tensor` of type `input_row_splits_dtype`.
    input_value_dtype: A `tf.dtypes.DType`.
    input_row_splits_dtype: A `tf.dtypes.DType`.

    Returns:
    A `Tensor` of type `variant`.
    """

    # Create a RaggedTensor from the input values and row splits
    input_ragged_tensor = tf.RaggedTensor.from_row_splits(values=input_values, row_splits=input_row_splits)

    # Encode the RaggedTensor into a variant Tensor
    encoded_variant_tensor = tf.raw_ops.EncodeRagged( 
        values=input_ragged_tensor.values, 
        axis=0, 
        splits=input_ragged_tensor.row_splits,
        dense_values_dtype=input_value_dtype,
        dense_splits_dtype=input_row_splits_dtype)

    return encoded_variant_tensor

# Example usage:
input_values = [1, 2, 3, 4, 5, 6]
input_row_splits = [0, 4, 4, 6, 8, 8]
input_value_dtype = tf.dtypes.int32
input_row_splits_dtype = tf.dtypes.int64

result = encode_ragged_tensor_to_variant(input_values, input_row_splits, input_value_dtype, input_row_splits_dtype)

print(result)
