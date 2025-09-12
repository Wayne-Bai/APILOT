import tensorflow as tf

def convert_raw_bytes_to_tensor(input_tensor, dtype):
    """
    Convert raw bytes from input tensor into numeric tensors.

    Args:
    input_tensor: tf.Tensor of type tf.string, where each element is a string
                  representation of a numeric value.
    dtype: tf.dtypes.DType, which specifies the numeric type to convert to.

    Returns:
    tf.Tensor of the specified dtype.
    """
    # Decode bytes to string
    decoded_tensor = tf.strings.decode(input_tensor, 'UTF-8')

    # Convert string to numeric tensor
    numeric_tensor = tf.strings.to_number(decoded_tensor, out_type=dtype)

    return numeric_tensor

# Example usage
if __name__ == "__main__":
    input_tensor = tf.constant(['1', '2', '3', '4'])

    converted_tensor = convert_raw_bytes_to_tensor(input_tensor, tf.float32)

    print(converted_tensor)
