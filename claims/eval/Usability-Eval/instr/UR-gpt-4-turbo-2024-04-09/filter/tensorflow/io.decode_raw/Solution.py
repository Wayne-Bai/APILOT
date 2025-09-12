import tensorflow as tf

def convert_raw_bytes_to_tensor(input_tensor):
    # Decode the raw bytes into a tensor
    decoded_tensor = tf.io.decode_raw(input_tensor, out_type=tf.float32)
    return decoded_tensor

# Example usage:
# Create a raw input tensor (simulate a byte string)
raw_input = tf.constant(b'\x00\x00\x80?', dtype=tf.string)

# Convert the raw bytes to a numeric tensor
numeric_tensor = convert_raw_bytes_to_tensor(raw_input)
print(numeric_tensor)
