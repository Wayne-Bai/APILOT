import tensorflow as tf

def convert_raw_bytes_to_numeric_tensor(raw_tensor):
    # Assuming raw_tensor is a 1-D tensor of bytes
    # Convert the raw bytes into a numeric representation (e.g., uint8)
    numeric_tensor = tf.io.decode_raw(raw_tensor, tf.uint8)

    return numeric_tensor

# Example usage:
raw_bytes = tf.constant([b'\x00\x01\x02\x03\x04', b'\x05\x06\x07\x08\x09'], dtype=tf.string)
numeric_tensor = convert_raw_bytes_to_numeric_tensor(raw_bytes)
print(numeric_tensor)
