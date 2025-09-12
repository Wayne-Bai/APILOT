import tensorflow as tf

# Example function to convert raw bytes to numeric tensors
def convert_raw_bytes(input_tensor, dtype=tf.float32, shape=None):
    # Create a decoder function
    def decode_bytes(bytes_tensor):
        return tf.io.decode_raw(bytes_tensor, out_type=dtype)
    
    # Map the decode function to input tensor
    decoded_tensor = tf.map_fn(decode_bytes, input_tensor, dtype=dtype)

    # Optional: If shape is provided, reshape the tensor
    if shape is not None:
        decoded_tensor = tf.reshape(decoded_tensor, shape)
    
    return decoded_tensor

# Example usage
# Create a mock tensor with raw bytes
raw_bytes = tf.constant([b'\x00\x00\x80?', b'\x00\x00\x00@'], dtype=tf.string)
numeric_tensor = convert_raw_bytes(raw_bytes, dtype=tf.float32)

# Print the tensor
print(numeric_tensor.numpy())
