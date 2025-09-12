import tensorflow as tf

def convert_bytes_to_tensor(input_bytes):
    # Decode bytes to a tensor of type uint8    '
    decoded_tensor = tf.io.decode_raw(input_bytes, out_type=tf.uint8)
    return decoded_tensor

# Example usage:
raw_bytes = tf.constant(b'\x01\x02\x03\x04', dtype=tf.string)
numeric_tensor = convert_bytes_to_tensor(raw_bytes)
print(numeric_tensor)
