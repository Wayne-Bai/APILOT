# Import necessary tensorflow module
import tensorflow as tf

# Function to convert raw bytes to numeric tensors
def raw_bytes_to_numeric(raw_bytes, dtype):
    """
    Convert raw bytes from input tensor into numeric tensors.

    Parameters:
    raw_bytes (tf.Tensor): Input tensor with raw bytes.
    dtype (tf.dtypes.DType): Data type to convert the raw bytes into.

    Returns:
    tf.Tensor: Numeric tensor converted from raw bytes.
    """
    # Convert raw bytes to numeric tensor
    numeric_tensor = tf.io.decode_raw(raw_bytes, dtype)

    return numeric_tensor

# Example usage
# Create a tensor with raw bytes
raw_bytes_tensor = tf.constant([0x12, 0x34, 0x56, 0x78], dtype=tf.string)

# Convert raw bytes to numeric tensor with specified dtype
numeric_tensor = raw_bytes_to_numeric(raw_bytes_tensor, tf.uint16)

print(numeric_tensor)
